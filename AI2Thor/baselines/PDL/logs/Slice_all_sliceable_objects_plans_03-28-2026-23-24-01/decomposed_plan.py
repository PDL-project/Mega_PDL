# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding apple.
# 2. Robot not at apple location.

# SubTask 1: Slice the Apple.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: apple(Location=CounterTop), knife(Location=Drawer)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding bread.
# 2. Robot not at bread location.
# 3. Robot not holding knife.

# SubTask 2: Slice the Bread.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: bread(Location=CounterTop), knife(Location=Drawer)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding tomato.
# 2. Robot not at tomato location.
# 3. Robot not holding knife.

# SubTask 3: Slice the Tomato.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: tomato(Location=CounterTop), knife(Location=Drawer)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.
# 3. Robot not holding knife.

# SubTask 4: Slice the Lettuce.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: lettuce(Location=CounterTop), knife(Location=Drawer)

# Task Slice all sliceable objects is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4