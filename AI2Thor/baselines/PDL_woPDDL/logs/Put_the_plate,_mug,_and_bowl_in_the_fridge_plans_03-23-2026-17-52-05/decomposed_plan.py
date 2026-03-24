# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Three items to be placed in the fridge, using different instances of the fridge for parallel execution.

# PARALLEL GROUP A — Fridge
# Initial condition:
#1. Robot not holding Plate
#2. Fridge is closed

# SubTask 1: Put the Plate in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: plate(Location=counterTop), fridge(Location=floor)

# PARALLEL GROUP B — Fridge (runs concurrently with Group A)
# Initial condition:
#1. Robot not holding Mug
#2. Fridge is closed

# SubTask 2: Put the Mug in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: mug(Location=counterTop), fridge(Location=floor)

# PARALLEL GROUP C — Fridge (runs concurrently with Group A and B)
# Initial condition:
#1. Robot not holding Bowl
#2. Fridge is closed

# SubTask 3: Put the Bowl in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: bowl(Location=counterTop), fridge(Location=floor)

# Task Put the plate, mug, and bowl in the fridge is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3