# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# PARALLEL GROUP A — Drawer1
# Initial condition:
#1. Robot not holding ButterKnife
#2. Drawer1 is closed

# SubTask 1: Put the ButterKnife in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: ButterKnife(Location=Drawer), Drawer1(Location=Floor)

# PARALLEL GROUP B — Drawer2
# Initial condition:
#1. Robot not holding Fork
#2. Drawer2 is closed

# SubTask 2: Put the Fork in Drawer2.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: Fork(Location=CounterTop), Drawer2(Location=Floor)

# PARALLEL GROUP C — Drawer3
# Initial condition:
#1. Robot not holding Spoon
#2. Drawer3 is closed

# SubTask 3: Put the Spoon in Drawer3.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: Spoon(Location=CounterTop), Drawer3(Location=Floor)

# PARALLEL GROUP D — Drawer4
# Initial condition:
#1. Robot not holding Knife
#2. Drawer4 is closed

# SubTask 4: Put the Knife in Drawer4.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: Knife(Location=CounterTop), Drawer4(Location=Floor)

# Task Put appropriate utensils in storage is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4