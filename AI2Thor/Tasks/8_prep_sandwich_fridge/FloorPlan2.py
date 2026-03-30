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

        return event
