"""
To check completion of subtasks in 4_clear_floor_kitchen task.
Also checks coverage of the task and success of the task.

Task: Clear the kitchen floor by placing items at their appropriate positions.
      Apple and Tomato are placed on the floor; pick them up and put them on CounterTop.

Subtasks:
    • NavigateTo(Apple)
    • PickUpObject(Apple)
    • NavigateTo(CounterTop) [with Apple in inventory]
    • PutObject(CounterTop) [with Apple in inventory]
    • NavigateTo(Tomato)
    • PickUpObject(Tomato)
    • NavigateTo(CounterTop) [with Tomato in inventory]
    • PutObject(CounterTop) [with Tomato in inventory]

Coverage:
    • Apple
    • Tomato
    • CounterTop
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        subtasks = [
            'NavigateTo(Apple)',
            'PickUpObject(Apple)',
            'NavigateTo(CounterTop, Apple)',
            'PutObject(CounterTop, Apple)',
            'NavigateTo(Tomato)',
            'PickUpObject(Tomato)',
            'NavigateTo(CounterTop, Tomato)',
            'PutObject(CounterTop, Tomato)',
        ]

        conditional_subtasks = [
            'NavigateTo(CounterTop, Apple)',
            'PutObject(CounterTop, Apple)',
            'NavigateTo(CounterTop, Tomato)',
            'PutObject(CounterTop, Tomato)',
        ]

        independent_subtasks = [
            'NavigateTo(Apple)',
            'PickUpObject(Apple)',
            'NavigateTo(Tomato)',
            'PickUpObject(Tomato)',
        ]

        coverage = ["Apple", "Tomato", "CounterTop"]
        interact_objects = ["Apple", "Tomato"]
        interact_receptacles = ["CounterTop"]

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
