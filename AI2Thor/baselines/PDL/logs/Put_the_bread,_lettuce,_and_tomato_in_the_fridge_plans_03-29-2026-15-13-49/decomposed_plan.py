# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks wherever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding bread
#2. Fridge is initially closed

# SubTask 1: Put the Bread in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: bread(Location=CounterTop), fridge(Location=Floor)

# Initial condition:
#1. Robot not holding lettuce
#2. Fridge is initially closed

# SubTask 2: Put the Lettuce in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: lettuce(Location=CounterTop), fridge(Location=Floor)

# Initial condition:
#1. Robot not holding tomato
#2. Fridge is initially closed

# SubTask 3: Put the Tomato in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: tomato(Location=CounterTop), fridge(Location=Floor)

# Task Put the bread, lettuce, and tomato in the fridge is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3