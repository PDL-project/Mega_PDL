"""
Task: Slice the Tomato and Lettuce onto the Plate, and clean the Cup and Mug

Two parallel chains:
  Chain A (sequential): Navigate to each vegetable → SliceObject
                        → PickupObject(sliced) → PutObject(Plate, sliced)
  Chain B (parallel to A): PickupObject(Cup/Mug) → CleanObject → PutObject(CounterTop)

Subtasks:
  • NavigateTo(Tomato)
  • SliceObject(Tomato)
  • PickUpObject(Tomato)       [picks up TomatoSliced]
  • PutObject(Plate, Tomato)
  • NavigateTo(Lettuce)
  • SliceObject(Lettuce)
  • PickUpObject(Lettuce)      [picks up LettuceSliced]
  • PutObject(Plate, Lettuce)
  • NavigateTo(Cup)
  • PickUpObject(Cup)
  • CleanObject(Cup)
  • PutObject(CounterTop, Cup)
  • NavigateTo(Mug)
  • PickUpObject(Mug)
  • CleanObject(Mug)
  • PutObject(CounterTop, Mug)

Coverage:
  • Tomato
  • Lettuce
  • Plate
  • Cup
  • Mug
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        subtasks = [
            # Chain A: slice vegetables onto plate
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "PickUpObject(Tomato)",
            "PutObject(Plate, Tomato)",
            "NavigateTo(Lettuce)",
            "SliceObject(Lettuce)",
            "PickUpObject(Lettuce)",
            "PutObject(Plate, Lettuce)",
            # Chain B: clean cup and mug
            "NavigateTo(Cup)",
            "PickUpObject(Cup)",
            "CleanObject(Cup)",
            "PutObject(CounterTop, Cup)",
            "NavigateTo(Mug)",
            "PickUpObject(Mug)",
            "CleanObject(Mug)",
            "PutObject(CounterTop, Mug)",
        ]

        conditional_subtasks = [
            "PutObject(Plate, Tomato)",
            "PutObject(Plate, Lettuce)",
            "PutObject(CounterTop, Cup)",
            "PutObject(CounterTop, Mug)",
        ]

        independent_subtasks = [
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "PickUpObject(Tomato)",
            "NavigateTo(Lettuce)",
            "SliceObject(Lettuce)",
            "PickUpObject(Lettuce)",
            "NavigateTo(Cup)",
            "PickUpObject(Cup)",
            "CleanObject(Cup)",
            "NavigateTo(Mug)",
            "PickUpObject(Mug)",
            "CleanObject(Mug)",
        ]

        coverage = ["Tomato", "Lettuce", "Plate", "Cup", "Mug"]
        interact_objects = ["Tomato", "Lettuce", "Cup", "Mug"]
        interact_receptacles = ["Plate", "CounterTop"]

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
