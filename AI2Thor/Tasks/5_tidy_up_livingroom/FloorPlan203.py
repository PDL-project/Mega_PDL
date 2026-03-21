"""
Pre-initialization for FloorPlan203 — 5_tidy_up_livingroom
All positions cross-verified from other FloorPlan203 task preinits.
Floor-level positions used where verified (y ≈ 0).
"""

class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # RemoteControl: floor-level, verified from 3_clear_table_to_sofa/FloorPlan203
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='RemoteControl|-01.27|+00.45|+03.29',
            position={'x': -1.2716063261032104, 'y': 0.0077530695125460625, 'z': 6.739828109741211}
        )
        # Watch: floor-level, verified from 3_clear_table_to_sofa/FloorPlan203
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Watch|+00.24|+00.55|+02.52',
            position={'x': 0.2394097000360489, 'y': 0.006279114633798599, 'z': 6.946480751037598}
        )
        # Book: sofa-level, verified from 3_clear_table_to_sofa/FloorPlan203
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Book|-03.72|+00.76|-00.64',
            position={'x': 0.44289106130599976, 'y': 0.5504924654960632, 'z': 2.3081116676330566}
        )
        # Pencil: near Book on sofa (estimate, same sofa surface)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Pencil|-04.49|+00.76|-00.19',
            position={'x': 0.5981862545013428, 'y': 0.550445556640625, 'z': 3.08017897605896}
        )
        # KeyChain: near Book on sofa (estimate, same sofa surface)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='KeyChain|+00.11|+00.45|+04.86',
            position={'x': 0.11712534725666046, 'y': 0.5515668988227844, 'z': 2.8745787143707275}
        )
        return event
