# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding apple.
# 2. Robot not at apple location.

# SubTask 1: Slice the Apple. 
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: apple(Location=fridge), knife(Location=counterTop)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding cup.
# 2. Robot not at cup location.

# SubTask 2: Wash the Cup. 
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: cup(Location=cabinet), sink(Location=floor)

# Task Slice all the fruits and wash all the cups is done.