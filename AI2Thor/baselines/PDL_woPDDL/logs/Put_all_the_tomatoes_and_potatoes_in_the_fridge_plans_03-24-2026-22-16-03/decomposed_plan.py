# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding Tomato
#2. Fridge is initially closed

# SubTask 1: Put the Tomato in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: tomato(Location=CounterTop), fridge(Location=Floor)

# Initial condition:
#1. Robot not holding Potato
#2. Fridge is initially closed

# SubTask 2: Put the Potato in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: potato(Location=CounterTop), fridge(Location=Floor)

# Task Put all the tomatoes and potatoes in the fridge is done.
# Parallel structure: SubTask 1 || SubTask 2