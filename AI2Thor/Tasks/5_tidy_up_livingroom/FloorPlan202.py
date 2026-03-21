"""
Pre-initialization for FloorPlan202 — 5_tidy_up_livingroom
All positions cross-verified from other FloorPlan202 task preinits.
"""

class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # KeyChain: verified from 1_put_remotecontrol_keys_watch_box/FloorPlan202
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='KeyChain|-01.01|+00.70|+03.53',
            position={'x': -1.00753915309906, 'y': 0.7043681740760803, 'z': 3.530571699142456}
        )
        # Watch: verified from 1_put_remotecontrol_keys_watch_box/FloorPlan202
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Watch|-01.22|+00.70|+03.47',
            position={'x': -1.2187483310699463, 'y': 0.7040449380874634, 'z': 3.471052408218384}
        )
        # Book: verified from 1_put_computer_book_remotecontrol_sofa/FloorPlan202
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Book|-01.94|+00.70|+03.61',
            position={'x': -1.9425640106201172, 'y': 0.7040524482727051, 'z': 3.612591505050659}
        )
        # RemoteControl: verified from 1_put_computer_book_remotecontrol_sofa/FloorPlan202
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='RemoteControl|-01.27|+00.44|+02.15',
            position={'x': -1.273537278175354, 'y': 0.4441750645637512, 'z': 2.1527974605560303}
        )
        # Laptop: verified from 1_put_computer_book_remotecontrol_sofa/FloorPlan202
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Laptop|-03.22|+00.61|+00.58',
            position={'x': -3.2156782150268555, 'y': 0.614728569984436, 'z': 0.582680344581604}
        )
        return event
