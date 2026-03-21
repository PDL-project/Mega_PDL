"""
Pre-initialization for FloorPlan209 — 5_tidy_up_livingroom
All positions cross-verified from other FloorPlan209 task preinits.
"""

class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # KeyChain: verified from 4_clear_couch_livingroom/FloorPlan209
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='KeyChain|-04.21|+00.32|-03.65',
            position={'x': -4.004233360290527, 'y': 0.3297809660434723, 'z': -2.7201120853424072}
        )
        # RemoteControl: verified from 1_put_remotecontrol_keys_watch_box/FloorPlan209
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='RemoteControl|-04.29|+00.33|-02.66',
            position={'x': -4.292991638183594, 'y': 0.3303918242454529, 'z': -2.663956880569458}
        )
        # Newspaper: floor-level, verified from 4_clear_couch_livingroom/FloorPlan209
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Newspaper|-04.24|+00.34|-02.16',
            position={'x': -6.341192245483398, 'y': 0.0065051838755607605, 'z': -0.6072340607643127}
        )
        # Book: table-level, verified from 3_put_all_school_supplies_sofa/FloorPlan209
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Book|-02.53|+00.70|-05.12',
            position={'x': -3.366100549697876, 'y': 0.6998944878578186, 'z': -5.1249680519104}
        )
        # Watch: verified from 4_clear_couch_livingroom/FloorPlan209
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Watch|-02.79|+00.58|-02.07',
            position={'x': -4.050622463226318, 'y': 0.33011940121650696, 'z': -1.9149408340454102}
        )
        # Pen: table-level, verified from 3_put_all_school_supplies_sofa/FloorPlan209
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Pen|-02.83|+00.70|-04.96',
            position={'x': -2.8290140628814697, 'y': 0.7048178315162659, 'z': -4.963045597076416}
        )
        # Laptop: verified from 1_put_computer_book_remotecontrol_sofa/FloorPlan209
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Laptop|-02.57|+00.58|-02.51',
            position={'x': -2.570798397064209, 'y': 0.5791771411895752, 'z': -2.512434244155884}
        )
        return event
