"""
Task: Make a tomato sandwich and clear the table

Two parallel chains:
  Chain A (sequential): Pickup Knife → SliceObject(Tomato)
                        → PickupObject(TomatoSliced) → PutObject(Plate, TomatoSliced)
                        → PickupObject(Bread) → PutObject(Plate, Bread)
  Chain B (parallel to A): Clear table items to appropriate places
                        → PickupObject(Mug/Cup) → PutObject(Sink, Mug/Cup)
                        → PickupObject(Fork/Spoon) → PutObject(Drawer, Fork/Spoon)

Subtasks:
  • NavigateTo(Knife)
  • PickUpObject(Knife)
  • NavigateTo(Tomato)
  • SliceObject(Tomato)
  • NavigateTo(Bread)
  • PickUpObject(Bread)
  • PutObject(Plate, Bread)
  • NavigateTo(Mug)
  • PickUpObject(Mug)
  • PutObject(SinkBasin, Mug)
  • NavigateTo(Cup)
  • PickUpObject(Cup)
  • PutObject(SinkBasin, Cup)
  • NavigateTo(Fork)
  • PickUpObject(Fork)
  • NavigateTo(Drawer) [with Fork]
  • OpenObject(Drawer) [with Fork]
  • PutObject(Drawer, Fork)
  • NavigateTo(Spoon)
  • PickUpObject(Spoon)
  • NavigateTo(Drawer) [with Spoon]
  • OpenObject(Drawer) [with Spoon]
  • PutObject(Drawer, Spoon)

Coverage:
  • Tomato
  • Bread
  • Mug
  • Cup
  • Fork
  • Spoon
  • Plate
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        subtasks = [
            # Chain A: sandwich
            "NavigateTo(Knife)",
            "PickUpObject(Knife)",
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "NavigateTo(Bread)",
            "PickUpObject(Bread)",
            "PutObject(Plate, Bread)",
            # Chain B: clear table
            "NavigateTo(Mug)",
            "PickUpObject(Mug)",
            "PutObject(SinkBasin, Mug)",
            "NavigateTo(Cup)",
            "PickUpObject(Cup)",
            "PutObject(SinkBasin, Cup)",
            "NavigateTo(Fork)",
            "PickUpObject(Fork)",
            "NavigateTo(Drawer, Fork)",
            "OpenObject(Drawer, Fork)",
            "PutObject(Drawer, Fork)",
            "NavigateTo(Spoon)",
            "PickUpObject(Spoon)",
            "NavigateTo(Drawer, Spoon)",
            "OpenObject(Drawer, Spoon)",
            "PutObject(Drawer, Spoon)",
        ]

        conditional_subtasks = [
            "PutObject(Plate, Bread)",
            "PutObject(SinkBasin, Mug)",
            "PutObject(SinkBasin, Cup)",
            "NavigateTo(Drawer, Fork)",
            "OpenObject(Drawer, Fork)",
            "PutObject(Drawer, Fork)",
            "NavigateTo(Drawer, Spoon)",
            "OpenObject(Drawer, Spoon)",
            "PutObject(Drawer, Spoon)",
        ]

        independent_subtasks = [
            "NavigateTo(Knife)",
            "PickUpObject(Knife)",
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "NavigateTo(Bread)",
            "PickUpObject(Bread)",
            "NavigateTo(Mug)",
            "PickUpObject(Mug)",
            "NavigateTo(Cup)",
            "PickUpObject(Cup)",
            "NavigateTo(Fork)",
            "PickUpObject(Fork)",
            "NavigateTo(Spoon)",
            "PickUpObject(Spoon)",
        ]

        coverage = ["Tomato", "Bread", "Mug", "Cup", "Fork", "Spoon", "Plate"]
        interact_objects = ["Bread", "Mug", "Cup", "Fork", "Spoon"]
        interact_receptacles = ["Plate", "SinkBasin", "Drawer"]

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
