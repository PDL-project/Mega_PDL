# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Two drawers available → distribute items across Drawer1 and Drawer2 for parallel execution.

# PARALLEL GROUP A — Drawer5
# Initial condition:
#1. Robot not holding Fork
#2. Drawer5 is closed

# SubTask 1: Put the Fork in Drawer5.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: fork(Location=CounterTop), drawer5(Location=Floor)

# PARALLEL GROUP B — Drawer6 (runs concurrently with Group A)
# Initial condition:
#1. Robot not holding Spoon
#2. Drawer6 is closed  ← different instance from Drawer5 → no dependency with Group A

# SubTask 2: Put the Spoon in Drawer6.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: spoon(Location=CounterTop), drawer6(Location=Floor)

# Task Put all the forks and spoons in the drawer is done.
# Parallel structure: SubTask 1 || SubTask 2