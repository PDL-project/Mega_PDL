"""
Pre-initialization for FloorPlan4 — 6_put_silverware_in_drawer
Scatters Fork, Spoon, ButterKnife, Ladle, Spatula on countertop.
"""


class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # Fork: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Fork|-00.46|+01.04|+01.78',
            position={'x': -0.46, 'y': 1.04, 'z': 1.78}
        )
        # Spoon: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spoon|-00.43|+01.04|+01.90',
            position={'x': -0.43, 'y': 1.04, 'z': 1.90}
        )
        # ButterKnife: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='ButterKnife|-02.63|+01.11|+00.60',
            position={'x': -2.00, 'y': 1.11, 'z': 0.60}
        )
        # Ladle: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Ladle|-01.95|+01.14|+00.45',
            position={'x': -1.95, 'y': 1.14, 'z': 0.45}
        )
        # Spatula: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spatula|-00.81|+01.12|+00.53',
            position={'x': -0.81, 'y': 1.12, 'z': 0.53}
        )
        return event
