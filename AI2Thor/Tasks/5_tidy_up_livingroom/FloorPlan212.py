"""
Pre-initialization for FloorPlan212 — 5_tidy_up_livingroom
All positions cross-verified from other FloorPlan212 task preinits.
Floor-level positions used where verified (y ≈ 0).
"""

class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # Pillow: floor-level, verified from 4_clear_couch_livingroom/FloorPlan212
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Pillow|+00.65|+00.39|+01.71',
            position={'x': -1.1589105129241943, 'y': 0.06653190404176712, 'z': 1.360148310661316}
        )
        # RemoteControl: floor-level, verified from 4_clear_couch_livingroom/FloorPlan212
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='RemoteControl|+01.88|+00.33|+01.73',
            position={'x': 3.6926870346069336, 'y': 0.0007512643933296204, 'z': 1.7323088645935059}
        )
        # Pencil: verified from 3_put_all_school_supplies_sofa/FloorPlan212
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Pencil|+03.89|+00.87|+01.18',
            position={'x': 2.53610897064209, 'y': 0.32378891110420227, 'z': 1.644966721534729}
        )
        # KeyChain: verified from 4_clear_couch_livingroom/FloorPlan212
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='KeyChain|+01.50|+00.47|+00.53',
            position={'x': 1.9540479183197021, 'y': 0.32807642221450806, 'z': 1.6930464506149292}
        )
        # Pen: verified from 4_clear_couch_livingroom/FloorPlan212
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Pen|+03.93|+00.87|+01.04',
            position={'x': 1.668033242225647, 'y': 0.3327394723892212, 'z': 1.6211962699890117}
        )
        return event
