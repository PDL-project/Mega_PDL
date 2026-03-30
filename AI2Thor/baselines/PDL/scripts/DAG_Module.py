"""
DAG Module for PDDL Plan Parallelism Analysis
LLM을 사용하여 서브태스크들 간 의존성을 분석하고 Subtask-level DAG를 생성
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, field, asdict
import openai


# Subtask-level DAG 데이터 구조

@dataclass
class SubtaskSummary:
    """서브테스크 하나를 요약한 정보(LLM이 만듦)"""
    id: int
    name: str
    objects: List[str] = field(default_factory=list)
    preconds: List[str] = field(default_factory=list)
    effects: List[str] = field(default_factory=list)

@dataclass
class SubtaskEdge:
    """서브태스크 간의 의존성 간선"""
    from_id: int
    to_id: int
    dependency_type: str
    reason: str = ""

@dataclass
class SubtaskDAG:
    """전체 작업(Task) 내 서브태스크들의 전체 DAG 구조"""
    task_name: str
    nodes: List[SubtaskSummary] = field(default_factory=list)
    edges: List[SubtaskEdge] = field(default_factory=list)
    parallel_groups: Dict[int, List[int]] = field(default_factory=dict)

    def to_dict(self) -> Dict:
        return {
            "task_name": self.task_name,
            "nodes": [asdict(n) for n in self.nodes],
            "edges": [asdict(e) for e in self.edges],
            "parallel_groups": self.parallel_groups
        }


class DAGGenerator:
    """LLM 기반 Subtask DAG 생성기"""

    def __init__(self, api_key_file: str = "api_key", gpt_version: str = "gpt-4o"):
        self.gpt_version = gpt_version
        self._setup_api(api_key_file)

    def _setup_api(self, api_key_file: str) -> None:
        """
        api_key_file:
        - "api_key" or "api_key.txt" 같은 이름을 받아도 됨
        실제 위치:
        - AI2Thor/baselines/PDL/api_key.txt (이 DAG_Module.py와 같은 폴더 기준)
        """
        here = Path(__file__).resolve().parent  # .../AI2Thor/baselines/PDL/scripts
        pdl_dir = here.parent                   # .../AI2Thor/baselines/PDL

        candidates = [
            Path(api_key_file).expanduser(),
            Path(api_key_file + ".txt").expanduser(),
            pdl_dir / api_key_file,
            pdl_dir / (api_key_file + ".txt"),
        ]

        for c in candidates:
            if c.exists() and c.is_file():
                openai.api_key = c.read_text().strip()
                return

        raise FileNotFoundError(f"[DAG] api key file not found. Tried: {[str(c) for c in candidates]}")

    def parse_action(self, action_str: str) -> Tuple[str, str, List[str]]:
        """PDDL 액션 문자열을 파싱 (액션타입, 로봇, 물체들 추출)"""
        action_str = re.sub(r'\s*\(\d+\)\s*$', '', action_str).strip()
        parts = action_str.split()
        if len(parts) < 2:
            return (action_str, '', [])
        action_type = parts[0].lower()
        robot = parts[1]
        objects = parts[2:] if len(parts) > 2 else []
        return (action_type, robot, objects)

    # ==========================================================
    # Subtask-level DAG (서브태스크 간 관계 분석)
    # ==========================================================

    def _create_subtask_summary_prompt(self, subtask_name: str, plan_actions: List[str],
                                       problem_content: str, precondition_content: str) -> str:
        actions_txt = "\n".join([f"- {a}" for a in plan_actions])

        prompt = (
            "You are a robotics task abstraction module.\n"
            "Given one SUBTASK's PDDL info and action plan, extract a compact summary.\n\n"
            f"SUBTASK NAME: {subtask_name}\n\n"
            f"PDDL Problem:\n{problem_content}\n\n"
            f"Precondition Info:\n{precondition_content}\n\n"
            f"Plan Actions:\n{actions_txt}\n\n"
            "Return JSON only with the following schema:\n"
            "{\n"
            '  "objects": ["..."],\n'
            '  "preconds": ["..."],\n'
            '  "effects": ["..."]\n'
            "}\n\n"
            "Rules:\n"
            "- objects: include key objects mentioned. IMPORTANT: preserve instance names exactly as they appear (e.g., 'fridge1', 'fridge2', 'drawer1', 'drawer2'). Do NOT generalize instance names to generic types (do NOT write 'fridge' if the plan says 'fridge1').\n"
            "- preconds: minimal natural-language conditions required before starting.\n"
            "- effects: minimal natural-language outcomes after completion.\n"
            "- Output ONLY valid JSON.\n"
        )
        return prompt

    def build_subtask_summary(self, subtask_id: int, subtask_name: str,
                             plan_actions: List[str], problem_content: str, precondition_content: str) -> SubtaskSummary:
        """LLM을 통해 서브태스크가 '무엇을 위해 하는 일인지' 요약 정보를 추출"""
        prompt = self._create_subtask_summary_prompt(subtask_name, plan_actions, problem_content, precondition_content)
        try:
            response = openai.chat.completions.create(
                model=self.gpt_version,
                messages=[
                    {"role": "system", "content": "Output ONLY valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1200,
                temperature=0
            )
            text = response.choices[0].message.content.strip()
            if "```json" in text:
                text = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL).group(1)
            elif "```" in text:
                text = re.search(r'```\s*(.*?)\s*```', text, re.DOTALL).group(1)

            data = json.loads(text)
            return SubtaskSummary(
                id=subtask_id,
                name=subtask_name,
                objects=data.get("objects", []) or [],
                preconds=data.get("preconds", []) or [],
                effects=data.get("effects", []) or []
            )
        except Exception as e:
            print(f"[Subtask] summary LLM error for {subtask_name}: {e}")
            # fallback: objects는 action에서 대충
            objs = []
            for a in plan_actions:
                _, _, o = self.parse_action(a)
                objs.extend(o)
            objs = sorted(list({x for x in objs if x}))
            return SubtaskSummary(id=subtask_id, name=subtask_name, objects=objs, preconds=[], effects=[])

    def _create_subtask_dag_prompt(self, task_name: str, summaries: List[SubtaskSummary], task_goal: str = "") -> str:
        lines = []
        for s in summaries:
            lines.append(
                f"{s.id}: name={s.name}\n"
                f"   objects={s.objects}\n"
                f"   preconds={s.preconds}\n"
                f"   effects={s.effects}\n"
            )
        summaries_txt = "\n".join(lines)

        fewshot = (
            "### Example A (HAS dependency: clear causal link)\n"
            "1: preconds=['container is closed'], effects=['container is open']\n"
            "2: preconds=['container is open'], effects=['item stored']\n"
            "Output:\n"
            "{\n"
            '  "dependencies": [\n'
            '    {"from": 1, "to": 2, "type": "causal", "reason": "Subtask 2 requires container to be open"}\n'
            "  ]\n"
            "}\n\n"

            "### Example B (NO dependency: completely different objects)\n"
            "1: objects=['document'], effects=['document archived']\n"
            "2: objects=['switch'], effects=['switch turned off']\n"
            "Output:\n"
            "{\n"
            '  "dependencies": []\n'
            "}\n\n"

            "### Example C (HAS dependency: SAME OBJECT manipulated sequentially)\n"
            "1: name='Wash the Fork', objects=['fork', 'sink'], effects=['fork is clean', 'fork at sink']\n"
            "2: name='Put Fork in Bowl', objects=['fork', 'bowl'], preconds=['fork is clean'], effects=['fork in bowl']\n"
            "Output:\n"
            "{\n"
            '  "dependencies": [\n'
            '    {"from": 1, "to": 2, "type": "causal", "reason": "Fork must be washed before putting in bowl"},\n'
            '    {"from": 1, "to": 2, "type": "resource", "reason": "Same fork object - cannot be manipulated in parallel"}\n'
            "  ]\n"
            "}\n\n"

            "### Example D (HAS dependency: object state change)\n"
            "1: objects=['apple'], effects=['robot holding apple']\n"
            "2: objects=['apple', 'fridge'], preconds=['robot holding apple'], effects=['apple in fridge']\n"
            "Output:\n"
            "{\n"
            '  "dependencies": [\n'
            '    {"from": 1, "to": 2, "type": "causal", "reason": "Must hold apple before putting in fridge"},\n'
            '    {"from": 1, "to": 2, "type": "binding", "reason": "Apple must be carried by same robot"}\n'
            "  ]\n"
            "}\n\n"
        )

        prompt = (
            "You are a multi-agent task planner.\n"
            "Given a list of SUBTASK summaries, determine subtask-level dependencies.\n"
            "Robot labels like 'robot1' are placeholders and MUST NOT create dependencies by themselves.\n\n"
            f"OVERALL TASK GOAL: {task_goal if task_goal else task_name}\n"
            "Use the overall task goal to understand the intended high-level order of operations "
            "when PDDL preconditions alone are insufficient to capture semantic dependencies.\n\n"
            f"{fewshot}"
            "SUBTASK SUMMARIES:\n"
            f"{summaries_txt}\n\n"
            "IMPORTANT: Use the EXACT subtask IDs as shown above. IDs are 1-based (starting from 1, NOT 0).\n\n"
            "Return JSON only with schema:\n"
            "{\n"
            '  "dependencies": [\n'
            '    {"from": <subtask_id>, "to": <subtask_id>, "type": "<causal|resource|binding|ordering>", "reason": "<brief>"},\n'
            "    ...\n"
            "  ]\n"
            "}\n\n"
            "DEPENDENCY DETECTION RULES (IMPORTANT!):\n"
            "1. SHARED TARGET RECEPTACLE INSTANCE = DEPENDENCY: If two subtasks PUT objects into the EXACT SAME receptacle instance\n"
            "   that must be OPENED/CLOSED (e.g., both use 'drawer1', or both use 'fridge1'), add a 'resource' dependency.\n"
            "   DIFFERENT instances of the same type = NO dependency (e.g., 'drawer1' vs 'drawer2', 'fridge1' vs 'fridge2' can run in PARALLEL).\n"
            "   EXCEPTION: CounterTop, DiningTable, Floor, Shelf are open surfaces — NO dependency even if both subtasks put objects on the same countertop.\n"
            "   Multiple robots can place different objects on the same countertop simultaneously.\n"
            "2. SAME MANIPULATED OBJECT: If two subtasks pick up / move / modify the SAME object (e.g., both use 'fork'),\n"
            "   add a 'resource' dependency.\n"
            "3. CAUSAL: If subtask B's precondition requires a state that subtask A's effect produces, add 'causal'.\n"
            "4. BINDING: If an object must be held/carried across subtasks (pickup in A, use in B), add 'binding'.\n\n"
            "RULES FOR NO DEPENDENCY (CRITICAL!):\n"
            "- SHARED SOURCE LOCATION is NOT a dependency. If subtasks pick up DIFFERENT objects from the same table/surface\n"
            "  (e.g., 'pick fork from diningTable' and 'pick mug from diningTable'), they CAN run in parallel.\n"
            "  A table/countertop/floor is a passive surface — multiple robots can pick up OR PUT DOWN different items simultaneously.\n"
            "- Generic shared locations (kitchen, floor, room) do NOT create dependencies.\n"
            "- Generic robot states ('robot not in action', 'robot not holding') do NOT create dependencies.\n"
            "- When in doubt, ask: 'Do both subtasks MODIFY the same object's state?' If not, NO dependency.\n\n"
            "Output ONLY valid JSON. No markdown.\n"
        )
        return prompt

    def build_subtask_dag(self, task_name: str, summaries: List[SubtaskSummary], task_goal: str = "") -> SubtaskDAG:
        """서브태스크 요약본을 비교하여 전체적인 실행 순서(Subtask DAG) 구축"""
        prompt = self._create_subtask_dag_prompt(task_name, summaries, task_goal=task_goal)
        try:
            response = openai.chat.completions.create(
                model=self.gpt_version,
                messages=[
                    {"role": "system", "content": "Output ONLY valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0
            )
            text = response.choices[0].message.content.strip()
            if "```json" in text:
                text = re.search(r'```json\s*(.*?)\s*```', text, re.DOTALL).group(1)
            elif "```" in text:
                text = re.search(r'```\s*(.*?)\s*```', text, re.DOTALL).group(1)

            data = json.loads(text)

            edges: List[SubtaskEdge] = []
            for d in data.get("dependencies", []):
                t = (d.get("type") or "").lower().strip()
                if t not in ("causal", "resource", "binding", "ordering"):
                    t = "causal"
                edges.append(SubtaskEdge(
                    from_id=int(d["from"]),
                    to_id=int(d["to"]),
                    dependency_type=t,
                    reason=d.get("reason", "")
                ))

            node_ids = [s.id for s in summaries]
            pg = self._compute_subtask_parallel_groups(node_ids, edges)

            return SubtaskDAG(
                task_name=task_name,
                nodes=summaries,
                edges=edges,
                parallel_groups=pg
            )
        except Exception as e:
            print(f"[Subtask] DAG LLM error: {e}")
            return SubtaskDAG(task_name=task_name, nodes=summaries, edges=[], parallel_groups={0: [s.id for s in summaries]})

    def _compute_subtask_parallel_groups(self, node_ids: List[int], edges: List[SubtaskEdge]) -> Dict[int, List[int]]:
        id_set = set(node_ids)
        preds = {i: set() for i in node_ids}
        succs = {i: set() for i in node_ids}

        for e in edges:
            u, v = e.from_id, e.to_id
            if u in id_set and v in id_set:
                preds[v].add(u)
                succs[u].add(v)

        from collections import deque
        indeg = {i: len(preds[i]) for i in node_ids}
        level = {i: 0 for i in node_ids}
        q = deque([i for i in node_ids if indeg[i] == 0])

        while q:
            u = q.popleft()
            for v in succs[u]:
                level[v] = max(level[v], level[u] + 1)
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        groups: Dict[int, List[int]] = {}
        for i in node_ids:
            groups.setdefault(level[i], []).append(i)
        return groups

    def save_subtask_dag_json(self, dag: SubtaskDAG, output_path: str) -> None:
        with open(output_path, "w") as f:
            json.dump(dag.to_dict(), f, indent=2, ensure_ascii=False)

    def visualize_subtask_dag(self, dag: SubtaskDAG, output_path: str) -> None:
        try:
            import pydot
        except ImportError:
            print("[Subtask] pydot not installed. Try: pip install pydot graphviz")
            return

        graph = pydot.Dot(graph_type="digraph", rankdir="TB", splines="spline", bgcolor="white")
        graph.set_node_defaults(shape="box", style="rounded,filled", fillcolor="white",
                                fontname="Helvetica", fontsize="10", margin="0.08,0.05")
        graph.set_edge_defaults(color="#555555", arrowsize="0.7", penwidth="1.2")

        group_nodes: Dict[int, List[str]] = {}
        node_to_group = {}
        for g, ids in dag.parallel_groups.items():
            for sid in ids:
                node_to_group[sid] = g

        for s in dag.nodes:
            gid = node_to_group.get(s.id, 0)
            label = f"{s.id}. {s.name}\\nobjs={len(s.objects)}"
            graph.add_node(pydot.Node(str(s.id), label=label))
            group_nodes.setdefault(gid, []).append(str(s.id))

        for g, ids in sorted(group_nodes.items()):
            sg = pydot.Cluster(
                graph_name=f"cluster_sub_g{g}",
                label=f"서브테스크 단위 병렬실행 그룹 {g}",
                color="#DDDDDD",
                style="rounded",
                fontname="Helvetica",
                fontsize="11",
                penwidth="1"
            )
            sg.add_node(pydot.Node("rank_dummy_sub_" + str(g), style="invis"))
            for nid in ids:
                sg.add_node(pydot.Node(nid))
            sg.set_rank("same")
            graph.add_subgraph(sg)

        for e in dag.edges:
            t = (e.dependency_type or "").lower()
            if t == "resource":
                style, color, penwidth = "dashed", "#757575", "1.2"
            elif t == "binding":
                style, color, penwidth = "bold", "#E53935", "2.5"
            elif t == "ordering":
                style, color, penwidth = "dotted", "#4E6CEF", "1.4"
            else:  # causal
                style, color, penwidth = "solid", "#333333", "1.2"

            graph.add_edge(pydot.Edge(
                str(e.from_id), str(e.to_id),
                style=style, color=color, penwidth=penwidth
            ))

        ext = os.path.splitext(output_path)[1].lower()
        if ext == ".pdf":
            graph.write_pdf(output_path)
        else:
            graph.write_png(output_path)


class DAGProcessor:
    """프로젝트 폴더 내의 모든 PDDL 계획 파일을 읽어 Subtask DAG를 생성하는 메인 프로세서"""

    def __init__(self, base_path: str, api_key_file: str = "api_key", gpt_version: str = "gpt-4o"):
        self.base_path = base_path
        self.generator = DAGGenerator(api_key_file, gpt_version)

        self.resources_path = os.path.join(base_path, "resources")
        self.plans_path = os.path.join(self.resources_path, "subtask_pddl_plans")
        self.problems_path = os.path.join(self.resources_path, "subtask_pddl_problems")
        self.preconditions_path = os.path.join(self.resources_path, "precondition_subtasks")
        self.output_path = os.path.join(self.resources_path, "dag_outputs", "dag")

        os.makedirs(self.output_path, exist_ok=True)

    def find_matching_files(self, plan_file: str) -> Tuple[Optional[str], Optional[str]]:
        base_name = plan_file.replace("_actions.txt", "").replace("_allocated.txt", "")
        problem_file = os.path.join(self.problems_path, f"{base_name}.pddl")
        precond_file = os.path.join(self.preconditions_path, base_name.replace("subtask_", "pre_") + ".txt")
        problem_path = problem_file if os.path.exists(problem_file) else None
        precond_path = precond_file if os.path.exists(precond_file) else None
        return problem_path, precond_path

    def process_all_plans(self, task_name: str = "task") -> SubtaskDAG:
        """모든 서브태스크 계획에 대해 Subtask DAG를 생성"""

        summaries: List[SubtaskSummary] = []

        plan_files = [f for f in os.listdir(self.plans_path) if f.endswith("_actions.txt")]

        for plan_file in sorted(plan_files):
            plan_path = os.path.join(self.plans_path, plan_file)
            with open(plan_path, 'r') as f:
                plan_actions = [line.strip() for line in f.readlines() if line.strip()]

            if not plan_actions:
                print(f"[DAG] Empty plan file: {plan_file}")
                continue

            problem_path, precond_path = self.find_matching_files(plan_file)
            problem_content = ""
            precond_content = ""

            if problem_path:
                with open(problem_path, 'r') as f:
                    problem_content = f.read()

            if precond_path:
                with open(precond_path, 'r') as f:
                    precond_content = f.read()

            m_sid = re.search(r"subtask_(\d+)", plan_file)
            subtask_id = int(m_sid.group(1)) if m_sid else len(summaries) + 1
            subtask_name = plan_file.replace("_actions.txt", "")

            s = self.generator.build_subtask_summary(
                subtask_id=subtask_id,
                subtask_name=subtask_name,
                plan_actions=plan_actions,
                problem_content=problem_content,
                precondition_content=precond_content
            )
            summaries.append(s)

        subtask_dag = self.generator.build_subtask_dag(task_name=task_name, summaries=summaries)

        subtask_json = os.path.join(self.output_path, f"{task_name}_SUBTASK_DAG.json")
        self.generator.save_subtask_dag_json(subtask_dag, subtask_json)

        subtask_img = os.path.join(self.output_path, f"{task_name}_SUBTASK_DAG.png")
        self.generator.visualize_subtask_dag(subtask_dag, subtask_img)

        return subtask_dag


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate Subtask DAG from PDDL plans")
    parser.add_argument("--base-path", type=str, default=os.getcwd(), help="Base path of the project")
    parser.add_argument("--api-key-file", type=str, default="api_key", help="OpenAI API key file")
    parser.add_argument("--gpt-version", type=str, default="gpt-4o", help="GPT model version")
    parser.add_argument("--task-name", type=str, default="task", help="Name for subtask-level DAG output files")
    args = parser.parse_args()

    processor = DAGProcessor(base_path=args.base_path, api_key_file=args.api_key_file, gpt_version=args.gpt_version)

    subtask_dag = processor.process_all_plans(task_name=args.task_name)

    print(f"\n[SubtaskDAG] {len(subtask_dag.nodes)} nodes, {len(subtask_dag.edges)} edges")
    for g, ids in sorted(subtask_dag.parallel_groups.items()):
        names = [n.name for n in subtask_dag.nodes if n.id in ids]
        print(f"  Group {g} (parallel): {names}")


if __name__ == "__main__":
    main()
