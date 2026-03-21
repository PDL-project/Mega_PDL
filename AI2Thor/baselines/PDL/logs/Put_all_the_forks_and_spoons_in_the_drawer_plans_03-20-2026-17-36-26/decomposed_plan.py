# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Since there is only one drawer available, tasks must be executed sequentially.

# Initial condition:
#1. Robot not holding Fork
#2. Drawer1 is closed

# SubTask 1: Put the Fork in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: Fork(Location=CounterTop), Drawer1(Location=Floor)

# Initial condition:
#1. Robot not holding Spoon
#2. Drawer1 is closed  ← same instance as SubTask 1 → sequential within this group

# SubTask 2: Put the Spoon in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: Spoon(Location=CounterTop), Drawer1(Location=Floor)

# Task Put all the forks and spoons in the drawer is done.
# Sequential structure: SubTask 1 → SubTask 2