"""
Checker for 6_put_silverware_in_drawer.
Goal: Put all forks, spoons, butter knives, and spatulas in a drawer.
Subtasks cover Navigate → PickUp → Navigate(Drawer) → Open → Put → Close per object.
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        subtasks = [
            'NavigateTo(Fork)',
            'PickUpObject(Fork)',
            'NavigateTo(Drawer, Fork)',
            'OpenObject(Drawer, Fork)',
            'PutObject(Drawer, Fork)',
            'NavigateTo(Spoon)',
            'PickUpObject(Spoon)',
            'NavigateTo(Drawer, Spoon)',
            'OpenObject(Drawer, Spoon)',
            'PutObject(Drawer, Spoon)',
            'NavigateTo(ButterKnife)',
            'PickUpObject(ButterKnife)',
            'NavigateTo(Drawer, ButterKnife)',
            'OpenObject(Drawer, ButterKnife)',
            'PutObject(Drawer, ButterKnife)',
            'NavigateTo(Spatula)',
            'PickUpObject(Spatula)',
            'NavigateTo(Drawer, Spatula)',
            'OpenObject(Drawer, Spatula)',
            'PutObject(Drawer, Spatula)',
        ]

        conditional_subtasks = [
            'NavigateTo(Drawer, Fork)',
            'OpenObject(Drawer, Fork)',
            'PutObject(Drawer, Fork)',
            'NavigateTo(Drawer, Spoon)',
            'OpenObject(Drawer, Spoon)',
            'PutObject(Drawer, Spoon)',
            'NavigateTo(Drawer, ButterKnife)',
            'OpenObject(Drawer, ButterKnife)',
            'PutObject(Drawer, ButterKnife)',
            'NavigateTo(Drawer, Spatula)',
            'OpenObject(Drawer, Spatula)',
            'PutObject(Drawer, Spatula)',
        ]

        independent_subtasks = [
            'NavigateTo(Fork)',
            'PickUpObject(Fork)',
            'NavigateTo(Spoon)',
            'PickUpObject(Spoon)',
            'NavigateTo(ButterKnife)',
            'PickUpObject(ButterKnife)',
            'NavigateTo(Spatula)',
            'PickUpObject(Spatula)',
        ]

        coverage = ['Fork', 'Spoon', 'ButterKnife', 'Spatula', 'Drawer']
        interact_objects = ['Fork', 'Spoon', 'ButterKnife', 'Spatula']
        interact_receptacles = ['Drawer']

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
