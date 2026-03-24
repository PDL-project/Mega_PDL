"""
Pre-initialization for FloorPlan3 — 7_put_ingredients_on_counter

preinit : 씬의 모든 식재료를 바닥에 분산 배치.
          → 기본 위치(countertop, fridge 등)에 있던 식재료를 전부 바닥으로 이동.
          → 로봇들이 서로 다른 위치로 퍼져서 집으러 가게끔 간격 확보.

perturb : planning 완료 후, 실행 직전에 자동 호출됨.
          Robot 2 손에 non-food 물체를 쥐어줌.
          → Robot 2가 식재료 집으려 할 때 "hand has something in it already" 실패
          → 재계획: 들고 있는 물체를 내려놓은 후 식재료 집기
"""

FOOD_TYPES = ['Bread', 'Tomato', 'Lettuce', 'Apple', 'Potato']
CANDIDATE_TYPES = ['Spoon', 'Fork', 'ButterKnife', 'Mug', 'Cup', 'Bowl', 'Pan', 'Pot', 'Plate']
MIN_SPACING = 1.0  # 식재료 간 최소 거리 (meter)


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

        # MIN_SPACING 이상 떨어진 위치만 골라서 분산 배치
        spread = []
        for pos in reachable:
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

        if not candidates:
            print("[PERTURB] No holdable objects found — skipping")
            return event

        obj = candidates[0]
        result = controller.step(
            action='PickupObject',
            objectId=obj['objectId'],
            agentId=1,  # Robot 2 (0-indexed)
            forceAction=True
        )
        print(f"[PERTURB] Robot2 holding {obj['objectType']}: {result.metadata['lastActionSuccess']}")

        return controller.last_event
