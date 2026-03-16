# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at any specific object location.

# SubTask 1: Move the Bowl to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: bowl(Location=diningTable), counterTop(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at any specific object location.

# SubTask 2: Move the ButterKnife to the Drawer.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: butterKnife(Location=diningTable), drawer(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at any specific object location.

# SubTask 3: Move the Fork to the Drawer.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: fork(Location=diningTable), drawer(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at any specific object location.

# SubTask 4: Move the Lettuce to the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: lettuce(Location=diningTable), fridge(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at any specific object location.

# SubTask 5: Move the Tomato to the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: tomato(Location=diningTable), fridge(Location=floor)

# Task Clear the table by placing items at their appropriate positions is done.