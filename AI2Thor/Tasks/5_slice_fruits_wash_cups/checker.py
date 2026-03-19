"""
Task: Slice all the fruits and wash all the cups

Two parallel chains:
  Chain A (sequential within): Navigate to each fruit → SliceObject
  Chain B (sequential within, parallel to A): PickupObject cup/mug/bowl → CleanObject → PutObject(CounterTop)

Subtasks:
  • NavigateTo(Apple)
  • SliceObject(Apple)
  • NavigateTo(Tomato)
  • SliceObject(Tomato)
  • NavigateTo(Lettuce)
  • SliceObject(Lettuce)
  • NavigateTo(Cup)
  • PickUpObject(Cup)
  • CleanObject(Cup)
  • PutObject(CounterTop, Cup)
  • NavigateTo(Mug)
  • PickUpObject(Mug)
  • CleanObject(Mug)
  • PutObject(CounterTop, Mug)
  • NavigateTo(Bowl)
  • PickUpObject(Bowl)
  • CleanObject(Bowl)
  • PutObject(CounterTop, Bowl)

Coverage:
  • Apple
  • Tomato
  • Lettuce
  • Cup
  • Mug
  • Bowl
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        subtasks = [
            "NavigateTo(Apple)",
            "SliceObject(Apple)",
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "NavigateTo(Lettuce)",
            "SliceObject(Lettuce)",
            "NavigateTo(Cup)",
            "PickUpObject(Cup)",
            "CleanObject(Cup)",
            "PutObject(CounterTop, Cup)",
            "NavigateTo(Mug)",
            "PickUpObject(Mug)",
            "CleanObject(Mug)",
            "PutObject(CounterTop, Mug)",
            "NavigateTo(Bowl)",
            "PickUpObject(Bowl)",
            "CleanObject(Bowl)",
            "PutObject(CounterTop, Bowl)",
        ]

        conditional_subtasks = [
            "PutObject(CounterTop, Cup)",
            "PutObject(CounterTop, Mug)",
            "PutObject(CounterTop, Bowl)",
        ]

        independent_subtasks = [
            "NavigateTo(Apple)",
            "SliceObject(Apple)",
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "NavigateTo(Lettuce)",
            "SliceObject(Lettuce)",
            "NavigateTo(Cup)",
            "PickUpObject(Cup)",
            "CleanObject(Cup)",
            "NavigateTo(Mug)",
            "PickUpObject(Mug)",
            "CleanObject(Mug)",
            "NavigateTo(Bowl)",
            "PickUpObject(Bowl)",
            "CleanObject(Bowl)",
        ]

        coverage = ["Apple", "Tomato", "Lettuce", "Cup", "Mug", "Bowl"]
        interact_objects = ["Cup", "Mug", "Bowl"]
        interact_receptacles = ["CounterTop"]

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
