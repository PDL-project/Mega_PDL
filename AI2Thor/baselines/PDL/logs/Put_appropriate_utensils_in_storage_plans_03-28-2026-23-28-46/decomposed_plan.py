# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Fork.
# 2. Robot not at Fork location.
# 3. Drawer1 is closed.

# SubTask 1: Put the Fork in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: fork(Location=CounterTop), drawer1(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Spoon.
# 2. Robot not at Spoon location.
# 3. Drawer2 is closed.

# SubTask 2: Put the Spoon in Drawer2.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: spoon(Location=CounterTop), drawer2(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Knife.
# 2. Robot not at Knife location.
# 3. Drawer3 is closed.

# SubTask 3: Put the Knife in Drawer3.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: knife(Location=CounterTop), drawer3(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Ladle.
# 2. Robot not at Ladle location.
# 3. Drawer4 is closed.

# SubTask 4: Put the Ladle in Drawer4.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: ladle(Location=CounterTop), drawer4(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Spatula.
# 2. Robot not at Spatula location.
# 3. Drawer5 is closed.

# SubTask 5: Put the Spatula in Drawer5.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: spatula(Location=CounterTop), drawer5(Location=Floor)

# Task Put appropriate utensils in storage is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5