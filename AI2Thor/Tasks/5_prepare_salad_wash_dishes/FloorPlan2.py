class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # Move Plate from cabinet to countertop (default: inside cabinet at y=1.67)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Plate|+01.32|+01.67|-01.60',
            position={'x': 0.0, 'y': 0.9157510995864868, 'z': 0.5},
        )

        # Move Cup from cabinet to countertop (default: inside cabinet at y=1.67)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Cup|+00.90|+01.67|-01.61',
            position={'x': 0.5, 'y': 0.9157510995864868, 'z': -0.28},
        )

        # Dirty Cup and Mug so CleanObject is meaningful
        event = controller.step(
            action='DirtyObject',
            objectId='Cup|+00.90|+01.67|-01.61',
            forceAction=True,
        )

        event = controller.step(
            action='DirtyObject',
            objectId='Mug|-00.24|+00.92|-00.26',
            forceAction=True,
        )

        return event
