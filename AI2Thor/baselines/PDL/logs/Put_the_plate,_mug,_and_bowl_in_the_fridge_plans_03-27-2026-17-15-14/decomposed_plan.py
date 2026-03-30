# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding plate
#2. Fridge is initially closed

# SubTask 1: Put the Plate in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: plate(Location=CounterTop), fridge(Location=Floor)

# Initial condition:
#1. Robot not holding mug
#2. Fridge is initially closed

# SubTask 2: Put the Mug in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: mug(Location=CounterTop), fridge(Location=Floor)

# Initial condition:
#1. Robot not holding bowl
#2. Fridge is initially closed

# SubTask 3: Put the Bowl in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: bowl(Location=CounterTop), fridge(Location=Floor)

# Task Put the plate, mug, and bowl in the fridge is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3