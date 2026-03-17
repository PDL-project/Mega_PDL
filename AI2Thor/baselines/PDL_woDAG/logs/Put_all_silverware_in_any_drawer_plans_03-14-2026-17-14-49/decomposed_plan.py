# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding fork.
# 2. Robot not at fork location.

# SubTask 1: Put the Fork in a Drawer. 
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: fork(Location=counterTop), drawer(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding spoon.
# 2. Robot not at spoon location.

# SubTask 2: Put the Spoon in a Drawer. 
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: spoon(Location=counterTop), drawer(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding knife.
# 2. Robot not at knife location.

# SubTask 3: Put the Knife in a Drawer. 
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: knife(Location=counterTop), drawer(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding butter knife.
# 2. Robot not at butter knife location.

# SubTask 4: Put the ButterKnife in a Drawer. 
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: butterKnife(Location=counterTop), drawer(Location=floor)

# Task Put all silverware in any drawer is done.