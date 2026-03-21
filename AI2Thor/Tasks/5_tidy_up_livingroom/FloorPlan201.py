"""
Pre-initialization for FloorPlan201 — 5_tidy_up_livingroom
Scatters KeyChain, Pen, Book, Pencil, Laptop on verified surface positions.
All positions cross-verified from other FloorPlan201 task preinits.
"""

class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # KeyChain: verified from 1_put_remotecontrol_keys_watch_box/FloorPlan201
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='KeyChain|-00.27|+00.70|+03.13',
            position={'x': -0.2682020068168640, 'y': 0.7014020085334778, 'z': 3.126955270767}
        )
        # Book: verified from 1_put_computer_book_remotecontrol_sofa/FloorPlan201 (sofa)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Book|-01.87|+00.68|+01.17',
            position={'x': -1.8720178604125977, 'y': 0.6790760755538940, 'z': 1.166492819786}
        )
        # Pencil: verified from 3_put_all_school_supplies_sofa/FloorPlan201 (sofa)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Pencil|-02.83|+00.68|+01.51',
            position={'x': -2.1178371906280518, 'y': 0.6001876592636108, 'z': 4.741385459899902}
        )
        # Pen: near Watch position from 1_put_remotecontrol_keys_watch_box/FloorPlan201
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Pen|-03.00|+00.69|+01.46',
            position={'x': -2.1016764640808105, 'y': 0.7336912155151367, 'z': -0.0577396973}
        )
        # Laptop: verified from 3_clear_table_to_sofa/FloorPlan201 (sofa)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Laptop|-01.70|+00.68|+01.66',
            position={'x': -2.0556342601776123, 'y': 0.5956512093544006, 'z': 5.12232208251}
        )
        return event
