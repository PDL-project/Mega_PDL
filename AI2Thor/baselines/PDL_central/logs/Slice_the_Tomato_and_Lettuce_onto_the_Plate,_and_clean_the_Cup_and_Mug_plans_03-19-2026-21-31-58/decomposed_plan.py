# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding tomato.
# 2. Robot not at tomato location.
# 3. Robot not holding knife.

# SubTask 1: Slice the Tomato onto the Plate.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=CounterTop), tomato(Location=CounterTop), plate(Location=CounterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.
# 3. Robot not holding knife.

# SubTask 2: Slice the Lettuce onto the Plate.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=CounterTop), lettuce(Location=Fridge), plate(Location=CounterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding cup.
# 2. Robot not at cup location.

# SubTask 3: Clean the Cup.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: cup(Location=Floor), sink(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding mug.
# 2. Robot not at mug location.

# SubTask 4: Clean the Mug.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: mug(Location=CounterTop), sink(Location=Floor)

# Task Slice the Tomato and Lettuce onto the Plate, and clean the Cup and Mug is done.