"""
Task: I want to eat a sandwich tomorrow. Please prepare and process the vegetables
      needed for making the sandwich, place them on a plate, and then store them
      in the refrigerator for use tomorrow.

Final target state (from MACE-THOR):
  - Lettuce: SLICED, on Plate
  - Tomato:  SLICED, on Plate
  - Plate:   contains [Lettuce, Tomato], in Fridge

Two parallel chains:
  Chain A: Navigate to Lettuce → SliceObject(Lettuce)
           → PickUpObject(Lettuce) → PutObject(Plate, Lettuce)
  Chain B: Navigate to Tomato  → SliceObject(Tomato)
           → PickUpObject(Tomato) → PutObject(Plate, Tomato)
  Chain C (after A & B): PickUpObject(Plate) → PutObject(Fridge, Plate)

Coverage:
  • Lettuce
  • Tomato
  • Plate
  • Fridge
"""

from AI2Thor.baselines.utils.checker import BaseChecker


class Checker(BaseChecker):
    def __init__(self) -> None:
        subtasks = [
            # Chain A: slice lettuce onto plate
            "NavigateTo(Lettuce)",
            "SliceObject(Lettuce)",
            "PickUpObject(Lettuce)",
            "PutObject(Plate, Lettuce)",
            # Chain B: slice tomato onto plate
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "PickUpObject(Tomato)",
            "PutObject(Plate, Tomato)",
            # Chain C: store plate in fridge
            "NavigateTo(Plate)",
            "PickUpObject(Plate)",
            "PutObject(Fridge, Plate)",
        ]

        conditional_subtasks = [
            "PutObject(Plate, Lettuce)",
            "PutObject(Plate, Tomato)",
            "PutObject(Fridge, Plate)",
        ]

        independent_subtasks = [
            "NavigateTo(Lettuce)",
            "SliceObject(Lettuce)",
            "PickUpObject(Lettuce)",
            "NavigateTo(Tomato)",
            "SliceObject(Tomato)",
            "PickUpObject(Tomato)",
            "NavigateTo(Plate)",
            "PickUpObject(Plate)",
        ]

        coverage = ["Lettuce", "Tomato", "Plate", "Fridge"]
        interact_objects = ["Lettuce", "Tomato", "Plate"]
        interact_receptacles = ["Plate", "Fridge"]

        super().__init__(
            subtasks,
            conditional_subtasks,
            independent_subtasks,
            coverage,
            interact_objects,
            interact_receptacles,
        )
