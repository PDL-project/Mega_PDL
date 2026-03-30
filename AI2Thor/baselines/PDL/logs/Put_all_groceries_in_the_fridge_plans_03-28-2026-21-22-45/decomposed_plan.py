# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition:
# 1. Robot not holding Apple.
# 2. Fridge is initially closed.

# SubTask 1: Put the Apple in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: apple(Location=CounterTop), fridge(Location=Floor)

# Initial Precondition:
# 1. Robot not holding Bread.
# 2. Fridge is initially closed.

# SubTask 2: Put the Bread in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: bread(Location=CounterTop), fridge(Location=Floor)

# Initial Precondition:
# 1. Robot not holding Lettuce.
# 2. Fridge is initially closed.

# SubTask 3: Put the Lettuce in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: lettuce(Location=CounterTop), fridge(Location=Floor)

# Initial Precondition:
# 1. Robot not holding Tomato.
# 2. Fridge is initially closed.

# SubTask 4: Put the Tomato in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: tomato(Location=CounterTop), fridge(Location=Floor)

# Initial Precondition:
# 1. Robot not holding Potato.
# 2. Fridge is initially closed.

# SubTask 5: Put the Potato in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: potato(Location=CounterTop), fridge(Location=Floor)

# Task Put all groceries in the fridge is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5