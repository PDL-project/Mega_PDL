# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Multiple drawers available → distribute items across Drawer1 and Drawer2 for parallel execution.

# PARALLEL GROUP A — Drawer1
# Initial condition:
#1. Robot not holding Fork
#2. Drawer1 is closed

# SubTask 1: Put the Fork in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: fork(Location=CounterTop), drawer1(Location=Floor)

# Initial condition:
#1. Robot not holding Spoon
#2. Drawer1 is closed  ← same instance as SubTask 1 → sequential within this group

# SubTask 2: Put the Spoon in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: spoon(Location=CounterTop), drawer1(Location=Floor)

# PARALLEL GROUP B — Drawer2 (runs concurrently with Group A)
# Initial condition:
#1. Robot not holding ButterKnife
#2. Drawer2 is closed  ← different instance from Drawer1 → no dependency with Group A

# SubTask 3: Put the ButterKnife in Drawer2.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: butterKnife(Location=CounterTop), drawer2(Location=Floor)

# Initial condition:
#1. Robot not holding Spatula
#2. Drawer2 is closed  ← same instance as SubTask 3 → sequential within this group

# SubTask 4: Put the Spatula in Drawer2.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: spatula(Location=CounterTop), drawer2(Location=Floor)

# Task Put all the forks, spoons, butter knives, and spatulas in the drawer is done.
# Parallel structure: [SubTask 1 → SubTask 2] || [SubTask 3 → SubTask 4]