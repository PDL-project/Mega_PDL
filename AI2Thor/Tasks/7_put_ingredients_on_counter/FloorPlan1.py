"""
Pre-initialization for FloorPlan1 — 7_put_ingredients_on_counter

preinit : 씬의 모든 식재료를 바닥에 분산 배치.
          → 기본 위치(countertop, fridge 등)에 있던 식재료를 전부 바닥으로 이동.
          → 로봇들이 서로 다른 위치로 퍼져서 집으러 가게끔 간격 확보.

perturb : planning 완료 후, 실행 직전에 자동 호출됨.
          Robot 1, Robot 2 손에 각각 다른 non-food 물체를 쥐어줌.
          → 두 로봇이 식재료 집으려 할 때 "hand has something in it already" 동시 실패
          → 두 재플래닝 그룹이 독립적으로 병렬 재계획 (per-replan-group lock 테스트용)
"""

FOOD_TYPES = ['Bread', 'Tomato', 'Lettuce', 'Apple', 'Potato']
CANDIDATE_TYPES = ['Spoon', 'Fork', 'ButterKnife', 'Mug', 'Cup', 'Bowl', 'Pan', 'Pot', 'Plate']
MIN_SPACING = 1.0   # 식재료 간 최소 거리 (meter)
ROBOT_CLEARANCE = 0.5  # 로봇 스폰 위치로부터 식재료 배치 제외 반경 (meter)


class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        food_objects = [
            o for o in controller.last_event.metadata['objects']
            if o['objectType'] in FOOD_TYPES and o.get('pickupable', False)
        ]
        if not food_objects:
            return controller.last_event

        # 도달 가능한 바닥 좌표 목록
        event = controller.step(action='GetReachablePositions')
        reachable = event.metadata.get('actionReturn', [])
        if not reachable:
            return controller.last_event

        # 현재 스폰된 로봇 위치 수집 (preinit은 로봇 스폰 후 호출)
        robot_positions = []
        for agent_event in controller.last_event.events:
            pos = agent_event.metadata.get('agent', {}).get('position', None)
            if pos:
                robot_positions.append(pos)

        def _too_close_to_robot(pos):
            return any(
                ((pos['x'] - rp['x']) ** 2 + (pos['z'] - rp['z']) ** 2) < ROBOT_CLEARANCE ** 2
                for rp in robot_positions
            )

        # MIN_SPACING 이상 떨어지고 로봇 위치와 겹치지 않는 위치만 선택
        spread = []
        for pos in reachable:
            if _too_close_to_robot(pos):
                continue
            if all(
                ((pos['x'] - p['x']) ** 2 + (pos['z'] - p['z']) ** 2) >= MIN_SPACING ** 2
                for p in spread
            ):
                spread.append(pos)
            if len(spread) >= len(food_objects):
                break

        for food, pos in zip(food_objects, spread):
            result = controller.step(
                action='PlaceObjectAtPoint',
                objectId=food['objectId'],
                position={'x': pos['x'], 'y': pos['y'] + 0.1, 'z': pos['z']}
            )
            print(f"[PREINIT] {food['objectType']} → floor ({pos['x']:.2f}, {pos['z']:.2f}): {result.metadata['lastActionSuccess']}")

        return controller.last_event

    def perturb(self, event, controller):
        candidates = [
            o for o in controller.last_event.metadata['objects']
            if o['objectType'] in CANDIDATE_TYPES and o.get('pickupable', False)
        ]

        TARGET_AGENTS = [0, 1]  # Robot 1, Robot 2 (0-indexed)
        for i, agent_idx in enumerate(TARGET_AGENTS):
            if i >= len(candidates):
                print(f"[PERTURB] Not enough holdable objects for Robot{agent_idx + 1} — skipping")
                continue
            obj = candidates[i]
            result = controller.step(
                action='PickupObject',
                objectId=obj['objectId'],
                agentId=agent_idx,
                forceAction=True
            )
            print(f"[PERTURB] Robot{agent_idx + 1} holding {obj['objectType']}: {result.metadata['lastActionSuccess']}")

        return controller.last_event
