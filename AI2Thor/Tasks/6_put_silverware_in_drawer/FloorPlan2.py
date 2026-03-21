"""
Pre-initialization for FloorPlan2 — 6_put_silverware_in_drawer
Scatters Fork, Spoon, ButterKnife, Ladle, Spatula on countertop.
"""


class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # Fork: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Fork|+01.69|+00.90|+01.45',
            position={'x': 1.69, 'y': 0.92, 'z': 1.45}
        )
        # Spoon: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spoon|+01.62|+00.90|+01.40',
            position={'x': 1.62, 'y': 0.92, 'z': 1.40}
        )
        # ButterKnife: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='ButterKnife|+01.67|+00.69|-00.11',
            position={'x': 1.67, 'y': 0.92, 'z': -0.11}
        )
        # Ladle: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Ladle|+01.79|+00.93|+01.13',
            position={'x': 1.79, 'y': 0.92, 'z': 1.13}
        )
        # Spatula: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spatula|+01.78|+00.91|-00.13',
            position={'x': 1.78, 'y': 0.92, 'z': -0.13}
        )
        return event
