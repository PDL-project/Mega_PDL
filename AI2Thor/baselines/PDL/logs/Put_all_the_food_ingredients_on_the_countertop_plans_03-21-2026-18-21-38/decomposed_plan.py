# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Apple.
# 2. Robot not at Apple location.

# SubTask 1: Put the Apple on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: apple(Location=fridge), countertop(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Lettuce.
# 2. Robot not at Lettuce location.

# SubTask 2: Put the Lettuce on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: lettuce(Location=fridge), countertop(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Egg.
# 2. Robot not at Egg location.

# SubTask 3: Put the Egg on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: egg(Location=counterTop), countertop(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Bread.
# 2. Robot not at Bread location.

# SubTask 4: Put the Bread on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: bread(Location=counterTop), countertop(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Tomato.
# 2. Robot not at Tomato location.

# SubTask 5: Put the Tomato on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: tomato(Location=counterTop), countertop(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Potato.
# 2. Robot not at Potato location.

# SubTask 6: Put the Potato on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: potato(Location=counterTop), countertop(Location=floor)

# Task Put all the food ingredients on the countertop is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5 || SubTask 6