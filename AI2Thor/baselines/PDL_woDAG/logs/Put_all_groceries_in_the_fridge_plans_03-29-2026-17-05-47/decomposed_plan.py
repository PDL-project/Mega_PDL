# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding apple.
# 2. Robot not at apple location.
# 3. Fridge is initially closed.

# SubTask 1: Put the Apple in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: apple(Location=CounterTop), fridge(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding bread.
# 2. Robot not at bread location.
# 3. Fridge is initially closed.

# SubTask 2: Put the Bread in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: bread(Location=CounterTop), fridge(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.
# 3. Fridge is initially closed.

# SubTask 3: Put the Lettuce in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: lettuce(Location=CounterTop), fridge(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding tomato.
# 2. Robot not at tomato location.
# 3. Fridge is initially closed.

# SubTask 4: Put the Tomato in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: tomato(Location=CounterTop), fridge(Location=Floor)

# Task Put all groceries in the fridge is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4