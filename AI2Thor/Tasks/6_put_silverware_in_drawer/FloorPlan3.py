"""
Pre-initialization for FloorPlan3 — 6_put_silverware_in_drawer
Scatters Fork, Spoon, ButterKnife, Spatula on countertop.
(FloorPlan3 has no Ladle/Knife — 4 utensils total)
"""


class SceneInitializer:
    def __init__(self) -> None:
        pass

    def preinit(self, event, controller):
        # Fork: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Fork|+00.62|+01.31|-02.48',
            position={'x': 0.62, 'y': 1.32, 'z': -2.48}
        )
        # Spoon: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spoon|+00.61|+01.32|-02.36',
            position={'x': 0.61, 'y': 1.32, 'z': -2.36}
        )
        # ButterKnife: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='ButterKnife|-01.57|+01.32|+01.35',
            position={'x': -1.57, 'y': 1.32, 'z': 1.35}
        )
        # Spatula: place on countertop (accessible)
        event = controller.step(
            action='PlaceObjectAtPoint',
            objectId='Spatula|-01.23|+01.32|-02.93',
            position={'x': -1.23, 'y': 1.32, 'z': -2.93}
        )
        return event
