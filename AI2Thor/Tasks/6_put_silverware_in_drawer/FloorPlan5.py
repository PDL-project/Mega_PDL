"""
Pre-initialization for FloorPlan5 — 6_put_silverware_in_drawer
Scatters Fork, Spoon, ButterKnife, Ladle, Spatula on countertop.
"""


class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # Fork: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Fork|-00.75|+00.90|+00.12',
            position={'x': -0.75, 'y': 0.90, 'z': 0.12}
        )
        # Spoon: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spoon|-00.06|+00.90|+00.10',
            position={'x': -0.06, 'y': 0.90, 'z': 0.10}
        )
        # ButterKnife: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='ButterKnife|-00.70|+00.90|+00.11',
            position={'x': -0.70, 'y': 0.90, 'z': 0.11}
        )
        # Ladle: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Ladle|-00.97|+01.14|+00.54',
            position={'x': -0.97, 'y': 1.14, 'z': 0.54}
        )
        # Spatula: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spatula|-00.93|+00.91|-00.18',
            position={'x': -0.93, 'y': 0.91, 'z': -0.18}
        )
        return event
