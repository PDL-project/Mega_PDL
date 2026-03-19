# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding tomato.
# 2. Robot not at tomato location.
# 3. Robot not holding knife.
# 4. Bowl is on the CounterTop.

# SubTask 1: Slice the Tomato into the Bowl.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=CounterTop), tomato(Location=CounterTop), bowl(Location=CounterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.
# 3. Robot not holding knife.
# 4. Bowl is on the CounterTop.

# SubTask 2: Slice the Lettuce into the Bowl.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=CounterTop), lettuce(Location=Fridge), bowl(Location=CounterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding cup.
# 2. Robot not at cup location.
# 3. Sink is on the Floor.

# SubTask 3: Clean the Cup.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: cup(Location=Cabinet), sink(Location=Floor)

# Task Slice the Tomato and Lettuce into the Bowl, and clean the Cup is done.