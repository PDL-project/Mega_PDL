# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding apple.
# 2. Robot not at apple location.

# SubTask 1: Put the Apple in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: apple(Location=counterTop), fridge(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding bread.
# 2. Robot not at bread location.

# SubTask 2: Put the Bread in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: bread(Location=counterTop), fridge(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.

# SubTask 3: Put the Lettuce in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: lettuce(Location=counterTop), fridge(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding tomato.
# 2. Robot not at tomato location.

# SubTask 4: Put the Tomato in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: tomato(Location=counterTop), fridge(Location=floor)

# Task Put all groceries in the fridge is done.