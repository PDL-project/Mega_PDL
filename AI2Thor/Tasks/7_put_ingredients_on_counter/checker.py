"""
Checker for 7_put_ingredients_on_counter.
Goal: Move all food ingredients (Bread, Tomato, Lettuce, Apple, Potato) onto the countertop.
Subtasks cover Navigate → PickUp → Navigate(CounterTop) → Put per object.
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        subtasks = [
            'NavigateTo(Bread)',
            'PickUpObject(Bread)',
            'NavigateTo(CounterTop, Bread)',
            'PutObject(CounterTop, Bread)',
            'NavigateTo(Tomato)',
            'PickUpObject(Tomato)',
            'NavigateTo(CounterTop, Tomato)',
            'PutObject(CounterTop, Tomato)',
            'NavigateTo(Lettuce)',
            'PickUpObject(Lettuce)',
            'NavigateTo(CounterTop, Lettuce)',
            'PutObject(CounterTop, Lettuce)',
            'NavigateTo(Apple)',
            'PickUpObject(Apple)',
            'NavigateTo(CounterTop, Apple)',
            'PutObject(CounterTop, Apple)',
            'NavigateTo(Potato)',
            'PickUpObject(Potato)',
            'NavigateTo(CounterTop, Potato)',
            'PutObject(CounterTop, Potato)',
        ]

        conditional_subtasks = [
            'NavigateTo(CounterTop, Bread)',
            'PutObject(CounterTop, Bread)',
            'NavigateTo(CounterTop, Tomato)',
            'PutObject(CounterTop, Tomato)',
            'NavigateTo(CounterTop, Lettuce)',
            'PutObject(CounterTop, Lettuce)',
            'NavigateTo(CounterTop, Apple)',
            'PutObject(CounterTop, Apple)',
            'NavigateTo(CounterTop, Potato)',
            'PutObject(CounterTop, Potato)',
        ]

        independent_subtasks = [
            'NavigateTo(Bread)',
            'PickUpObject(Bread)',
            'NavigateTo(Tomato)',
            'PickUpObject(Tomato)',
            'NavigateTo(Lettuce)',
            'PickUpObject(Lettuce)',
            'NavigateTo(Apple)',
            'PickUpObject(Apple)',
            'NavigateTo(Potato)',
            'PickUpObject(Potato)',
        ]

        coverage = ['Bread', 'Tomato', 'Lettuce', 'Apple', 'Potato', 'CounterTop']
        interact_objects = ['Bread', 'Tomato', 'Lettuce', 'Apple', 'Potato']
        interact_receptacles = ['CounterTop']

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
