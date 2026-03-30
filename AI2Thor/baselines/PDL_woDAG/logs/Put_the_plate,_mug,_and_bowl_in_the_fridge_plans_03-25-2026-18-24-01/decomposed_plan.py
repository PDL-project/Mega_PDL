# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Three items to be placed in the fridge, but only one fridge available → sequential execution required.

# Initial condition:
#1. Robot not holding Plate
#2. Fridge is closed

# SubTask 1: Put the Plate in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: plate(Location=counterTop), fridge(Location=floor)

# Initial condition:
#1. Robot not holding Mug
#2. Fridge is closed  ← same instance as SubTask 1 → sequential execution required

# SubTask 2: Put the Mug in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: mug(Location=counterTop), fridge(Location=floor)

# Initial condition:
#1. Robot not holding Bowl
#2. Fridge is closed  ← same instance as SubTask 1 and SubTask 2 → sequential execution required

# SubTask 3: Put the Bowl in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: bowl(Location=counterTop), fridge(Location=floor)

# Task Put the plate, mug, and bowl in the fridge is done.
# Sequential structure: SubTask 1 → SubTask 2 → SubTask 3