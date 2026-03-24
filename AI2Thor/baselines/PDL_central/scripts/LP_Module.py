# 작업할당 모듈 (LLM 기반)
from __future__ import annotations
from typing import Dict, List, Any, Tuple, Optional, Set
import ast
import json
import math
import re

# ----------------------------
# 로봇들의 능력 추출 함수 모음 부분
# ----------------------------

def get_capacity(robot_info: dict) -> float:
    """
    robots.py가 mass / mass_capacity 섞여있어서 통일해서 읽어오는 함수
    """
    if "mass_capacity" in robot_info:
        return float(robot_info["mass_capacity"])
    if "mass" in robot_info:
        return float(robot_info["mass"])
    return 0.0


def robot_capacity_map(robot_ids: List[int], robots_db: List[dict]) -> Dict[int, float]:
    """
    각 로봇 ID별로 들 수 있는 최대 무게 값을 매핑
    """
    return {rid: get_capacity(robots_db[rid - 1]) for rid in robot_ids}


# ----------------------------
# 환경 object 정보 추출 함수 모음
# ----------------------------

def parse_objects_ai(objects_ai: Any) -> List[dict]:
    """
    LLM이 생성한 물체 정보 데이터를 파이썬의 리스트 객체로 변환

    objects_ai가
    - 이미 list[dict]일 수도 있고
    - 문자열로 "objects = [...]" 형태일 수도 있어서 안전 파싱
    """
    if isinstance(objects_ai, list):
        return objects_ai

    if isinstance(objects_ai, str):
        s = objects_ai.strip()
        # "objects = [...]" 형태면 '=' 뒤만 파싱
        if "=" in s:
            s = s.split("=", 1)[1].strip()
        # python literal list 파싱 (json이 아닌 경우가 많아서)
        try:
            data = ast.literal_eval(s)
            if isinstance(data, list):
                return data
        except Exception:
            pass

    return []


def build_mass_map(objects_ai: Any) -> Dict[str, float]:
    """
    물체 리스트를 순회하며 각 물체의 이름과 무게를 매핑한 딕셔너리를 만드는 함수 (예: {'apple': 0.5})
    """
    objs = parse_objects_ai(objects_ai)
    mass_map: Dict[str, float] = {}
    for o in objs:
        name = str(o.get("name", "")).strip().lower()
        if not name:
            continue
        mass = float(o.get("mass", 0.0) or 0.0)
        mass_map[name] = mass
    return mass_map


# -----------------------------------------
# plan -> 옮겨야하는 오브젝트들의 무게를 계산하는 함수 모음
# -----------------------------------------

def _tok(action_line: str) -> List[str]:
    # 액션 문장(예: pickupobject robot1 apple...)에서 괄호를 제거하고 단어 단위로 쪼개주는 보조 함수
    return action_line.replace("(", " ").replace(")", " ").split()

def picked_objects_from_plan(plan_actions: List[str]) -> Set[str]:
    """
    한 서브태스크의 전체 액션 중 pickup, put, throw 등 물체를 손에 들고 있어야 하는 동작에서 대상 물체들을 추출
    """
    picked: Set[str] = set()
    for a in plan_actions:
        parts = _tok(a)
        if len(parts) < 3:
            continue
        at = parts[0].strip().lower()

        # pickupobject robotX OBJ ...
        if at == "pickupobject" and len(parts) >= 3:
            picked.add(parts[2].strip().lower())

        # put / throw / drop 류도 OBJ를 들고 있었을 가능성이 높으니 포함
        elif at in ("putobject", "putobjectinfridge", "throwobject", "drophandobject") and len(parts) >= 3:
            picked.add(parts[2].strip().lower())

    return picked


def required_mass_from_plan(plan_actions: List[str], mass_map: Dict[str, float]) -> float:
    """
    위에서 추출된 물체들의 무게를 합산하여, 이 작업을 수행할 로봇이 견뎌야 하는 총 무게를 계산하는 함수
    """
    objs = picked_objects_from_plan(plan_actions)
    return sum(float(mass_map.get(o, 0.0)) for o in objs)


# -----------------------------------------
# subtask -> subtask 간의 binding 관계 체크 함수
# -----------------------------------------

def binding_pairs_from_subtask_dag(subtask_dag: Any) -> List[Tuple[int, int]]:
    """
    서브태스크 DAG에서 binding 타입의 엣지를 찾아 "이 작업들은 반드시 같은 로봇이 해야 함"이라는 쌍(Pair) 리스트를 만드는 함수

    SubtaskDAG 구조-> dag.edges에 dependency_type 안에 해당 정보가 들어있음
    type == "binding" 인 엣지는 '같은 로봇 강제'로 처리
    """
    pairs: List[Tuple[int, int]] = []
    if subtask_dag is None:
        return pairs

    for e in getattr(subtask_dag, "edges", []) or []:
        # edges는 SubtaskEdge 객체일 수도 있고, JSON 로드된 dict일 수도 있음
        if isinstance(e, dict):
            t = (e.get("dependency_type", "") or "").lower().strip()
            from_id = e.get("from_id")
            to_id = e.get("to_id")
        else:
            t = (getattr(e, "dependency_type", "") or "").lower().strip()
            from_id = getattr(e, "from_id", None)
            to_id = getattr(e, "to_id", None)
        if t == "binding" and from_id is not None and to_id is not None:
            pairs.append((int(from_id), int(to_id)))

    # 중복 제거
    pairs = sorted(list({(a, b) for (a, b) in pairs}))
    return pairs


# -----------------------------------------
# 거리 계산 함수 모음
# -----------------------------------------

def _euclidean_dist(p1: Tuple[float, float, float], p2: Tuple[float, float, float]) -> float:
    """3D 유클리드 거리"""
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)


def build_position_map(objects_ai: Any) -> Dict[str, Tuple[float, float, float]]:
    """
    objects_ai에서 오브젝트별 좌표 딕셔너리 생성 (예: {'apple': (1.0, 0.9, -2.3)})
    """
    objs = parse_objects_ai(objects_ai)
    pos_map: Dict[str, Tuple[float, float, float]] = {}
    for o in objs:
        name = str(o.get("name", "")).strip().lower()
        pos = o.get("position", {})
        if name and pos:
            pos_map[name] = (float(pos.get("x", 0.0)), float(pos.get("y", 0.0)), float(pos.get("z", 0.0)))
    return pos_map


def first_target_object_from_plan(plan_actions: List[str]) -> Optional[str]:
    """
    서브태스크 플랜에서 첫 번째로 이동해야 할 대상 오브젝트를 추출
    gotoobject가 있으면 그 대상, 없으면 첫 번째 액션의 대상 오브젝트 반환
    """
    for a in plan_actions:
        parts = _tok(a)
        if len(parts) >= 3 and parts[0].strip().lower() == "gotoobject":
            return parts[2].strip().lower()
    # gotoobject 없으면 첫 번째 액션의 대상
    for a in plan_actions:
        parts = _tok(a)
        if len(parts) >= 3:
            return parts[2].strip().lower()
    return None


# ======================================================
# LLM 응답 파싱 헬퍼
# ======================================================

def _parse_assignment_from_llm(text: str, sids: List[int], robot_ids: List[int]) -> Dict[int, int]:
    """
    LLM 응답 텍스트에서 {subtask_id: robot_id} 딕셔너리를 추출한다.

    여러 JSON 블록이 있을 수 있으므로 가장 마지막 JSON 객체를 사용한다.
    키·값은 정수로 변환하며, 유효하지 않은 항목은 무시한다.
    """
    # 모든 JSON 객체 후보를 뒤에서부터 탐색
    candidates = list(re.finditer(r'\{[^{}]+\}', text, re.DOTALL))
    for m in reversed(candidates):
        try:
            raw = json.loads(m.group())
            result: Dict[int, int] = {}
            for k, v in raw.items():
                try:
                    sid = int(k)
                    rid = int(v)
                    if sid in sids and rid in robot_ids:
                        result[sid] = rid
                except (ValueError, TypeError):
                    continue
            if result:
                return result
        except json.JSONDecodeError:
            continue

    raise ValueError(f"LLM 응답에서 유효한 할당 JSON을 파싱할 수 없습니다.\n응답:\n{text}")


# ======================================================
# 메인 프로세스 — LLM 기반 작업할당 함수
# ======================================================

def assign_subtasks_llm(
    subtasks: List[dict],
    robot_ids: List[int],
    robots_db: List[dict],
    plan_actions_by_subtask: Dict[int, List[str]],
    objects_ai: Any,
    llm,           # LLMHandler (PDDL_Module.LLMHandler)
    gpt_version: str,
    binding_pairs: Optional[List[Tuple[int, int]]] = None,
    robot_positions: Optional[Dict[int, Tuple[float, float, float]]] = None,
    object_positions: Optional[Dict[str, Tuple[float, float, float]]] = None,
    parallel_groups: Optional[Dict[str, List[int]]] = None,
    forced_assignments: Optional[Dict[int, int]] = None,
    holding_exclusions: Optional[Dict[int, List[int]]] = None,
) -> Dict[int, int]:
    """
    LLM에게 subtask → robot 할당을 요청한다.

    Returns:
        {subtask_id: robot_id}

    Hard constraints (프롬프트에 명시):
      1) 로봇은 한 번에 한 가지 일만 할 수 있음
      2) 무게 제약 (required_mass <= robot capacity)
      3) Binding 쌍: 두 서브태스크는 반드시 같은 로봇
      4) Forced assignment: 특정 서브태스크는 반드시 특정 로봇 (물건을 이미 들고 있는 경우)

    Soft preferences (프롬프트에 명시):
      - 병렬 그룹 내 서브태스크는 가능한 한 다른 로봇에 분산
      - 로봇 간 작업 수 균등 분배 (로드 밸런싱)
      - 로봇↔대상 오브젝트 거리가 짧은 로봇 우선
    """
    sids = [int(st["id"]) for st in subtasks]

    # ---- 무게 정보 계산 ----
    mass_map = build_mass_map(objects_ai)
    cap = robot_capacity_map(robot_ids, robots_db)

    req_mass: Dict[int, float] = {}
    for sid in sids:
        plan = plan_actions_by_subtask.get(sid, [])
        req_mass[sid] = required_mass_from_plan(plan, mass_map)

    # ---- 거리 정보 계산 ----
    dist_info: Dict[int, Dict[int, float]] = {}  # dist_info[sid][rid] = distance
    if robot_positions and object_positions:
        for sid in sids:
            plan = plan_actions_by_subtask.get(sid, [])
            target_obj = first_target_object_from_plan(plan)
            obj_pos = object_positions.get(target_obj) if target_obj else None
            dist_info[sid] = {}
            for rid in robot_ids:
                if obj_pos and rid in robot_positions:
                    dist_info[sid][rid] = round(_euclidean_dist(robot_positions[rid], obj_pos), 2)
                else:
                    dist_info[sid][rid] = 0.0

    # ---- 프롬프트 구성 ----
    lines: List[str] = []

    # 1) 로봇 정보
    lines.append("## Robots")
    for rid in robot_ids:
        robot_info = robots_db[rid - 1]
        skills = robot_info.get("skills", [])
        skills_str = ", ".join(skills) if skills else "general"
        lines.append(
            f"- Robot {rid}: mass_capacity={cap[rid]:.2f}kg, skills=[{skills_str}]"
        )

    # 2) 서브태스크 정보
    lines.append("\n## Subtasks")
    for st in subtasks:
        sid = int(st["id"])
        title = st.get("title", f"Subtask_{sid}")
        plan = plan_actions_by_subtask.get(sid, [])
        actions_preview = "; ".join(plan[:5]) + ("..." if len(plan) > 5 else "")

        # 무게 제약 적용 가능한 로봇 목록
        feasible_robots = [rid for rid in robot_ids if req_mass[sid] <= cap[rid] + 1e-9]

        dist_str = ""
        if sid in dist_info:
            dist_parts = [f"Robot{rid}={d:.2f}m" for rid, d in dist_info[sid].items()]
            dist_str = f"  distances=[{', '.join(dist_parts)}]"

        lines.append(
            f"- Subtask {sid} ({title}): required_mass={req_mass[sid]:.2f}kg"
            f"  feasible_robots={feasible_robots}"
            f"  actions=[{actions_preview}]"
            f"{dist_str}"
        )

    # 3) Hard constraints
    lines.append("\n## Hard Constraints")

    if binding_pairs:
        lines.append(
            "- Binding pairs (MUST be assigned to the SAME robot): "
            + str(binding_pairs)
        )
    else:
        lines.append("- Binding pairs: none")

    if forced_assignments:
        fa_str = ", ".join(f"subtask {sid} → Robot {rid}" for sid, rid in forced_assignments.items())
        lines.append(f"- Forced assignments (robot already holding object): {fa_str}")
    else:
        lines.append("- Forced assignments: none")

    if holding_exclusions:
        ex_parts = []
        for rid, excl_sids in holding_exclusions.items():
            ex_parts.append(f"Robot {rid} CANNOT be assigned to subtasks {excl_sids} (hand is full, cannot pick up another object)")
        lines.append("- Holding exclusions (MUST NOT assign): " + "; ".join(ex_parts))
    else:
        lines.append("- Holding exclusions: none")

    # 4) Soft preferences
    lines.append("\n## Soft Preferences (apply in this priority order)")
    lines.append("1. [HIGHEST] Distribute parallel-group subtasks across different robots when possible.")
    if parallel_groups:
        for gk, gsids in parallel_groups.items():
            lines.append(f"   Group '{gk}': subtasks {gsids}")
    else:
        lines.append("   No parallel groups defined.")
    lines.append("2. Balance workload evenly across robots (minimize max load).")
    lines.append("3. Prefer assigning a subtask to the robot closest to its first target object.")

    # 5) 출력 형식
    lines.append("\n## Output")
    lines.append(
        "Return ONLY a single JSON object (no explanation, no code block) "
        "mapping each subtask_id (string key) to robot_id (integer value). "
        "All subtasks must be assigned. Example: "
        '{"1": 1, "2": 2, "3": 1}'
    )
    lines.append(f"Subtask IDs to assign: {sids}")
    lines.append(f"Valid robot IDs: {robot_ids}")

    user_content = "\n".join(lines)

    system_content = (
        "You are a Robot Task Allocation Expert. "
        "Each robot can work on only one subtask at a time. Assign each subtask to one robot while strictly satisfying all hard constraints. "
        "Among all feasible assignments, optimise for the soft preferences in the stated priority order. "
        "Output only the JSON assignment object — no additional text."
    )

    messages = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content},
    ]

    # ---- LLM 호출 ----
    _, text = llm.query_model(messages, gpt_version, max_tokens=512, temperature=0, frequency_penalty=0.0)

    # ---- 응답 파싱 ----
    assignment = _parse_assignment_from_llm(text, sids, robot_ids)

    # 누락된 서브태스크 확인
    missing = [sid for sid in sids if sid not in assignment]
    if missing:
        raise RuntimeError(
            f"LLM이 다음 서브태스크에 대한 할당을 반환하지 않았습니다: {missing}\n"
            f"LLM 응답:\n{text}"
        )

    return assignment
