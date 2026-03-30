# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding bread.
# 2. Robot not at bread location.

# SubTask 1: Slice the Bread.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: Bread(Location=CounterTop), Knife(Location=Drawer)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.
# 3. Robot not holding knife.

# SubTask 2: Slice the Lettuce.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: Lettuce(Location=CounterTop), Knife(Location=Drawer)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding tomato.
# 2. Robot not at tomato location.
# 3. Robot not holding knife.

# SubTask 3: Slice the Tomato.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: Tomato(Location=CounterTop), Knife(Location=Drawer)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding egg.
# 2. Robot not at egg location.
# 3. Robot not holding knife.

# SubTask 4: Slice the Egg.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: Egg(Location=CounterTop), Knife(Location=Drawer)

# Task Slice the bread, lettuce, tomato, and egg is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4