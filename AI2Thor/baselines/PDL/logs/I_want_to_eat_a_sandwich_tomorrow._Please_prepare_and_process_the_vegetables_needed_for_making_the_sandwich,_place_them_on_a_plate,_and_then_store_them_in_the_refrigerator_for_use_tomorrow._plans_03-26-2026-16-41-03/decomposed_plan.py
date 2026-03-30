# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.

# SubTask 1: Slice the Lettuce.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=CounterTop), lettuce(Location=Fridge)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding tomato.
# 2. Robot not at tomato location.
# 3. Robot not holding knife.

# SubTask 2: Slice the Tomato.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=CounterTop), tomato(Location=CounterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding bread.
# 2. Robot not at bread location.

# SubTask 3: Slice the Bread.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=CounterTop), bread(Location=CounterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding plate.
# 2. Robot not at plate location.

# SubTask 4: Place Sliced Vegetables on Plate.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: plate(Location=CounterTop), lettuce(Location=CounterTop), tomato(Location=CounterTop), bread(Location=CounterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding plate.
# 2. Fridge is initially closed.

# SubTask 5: Store the Plate with Sliced Vegetables in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: plate(Location=CounterTop), fridge(Location=Floor)

# Task I want to eat a sandwich tomorrow. Please prepare and process the vegetables needed for making the sandwich, place them on a plate, and then store them in the refrigerator for use tomorrow is done.
# Parallel structure: [SubTask 1 || SubTask 2 || SubTask 3] → SubTask 4 → SubTask 5