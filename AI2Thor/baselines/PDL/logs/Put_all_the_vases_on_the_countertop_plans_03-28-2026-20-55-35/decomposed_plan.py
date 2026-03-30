# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Two vases available → distribute tasks across different CounterTops for parallel execution.

# PARALLEL GROUP A — CounterTop1
# Initial condition:
#1. Robot not holding Vase1
#2. Vase1 is on the Shelf

# SubTask 1: Put Vase1 on CounterTop1.
    Skills Required: GoToObject, PickupObject, GoToObject, PutObject
    Related Objects: vase1(Location=shelf), countertop1(Location=floor)

# PARALLEL GROUP B — CounterTop2 (runs concurrently with Group A)
# Initial condition:
#1. Robot not holding Vase2
#2. Vase2 is on the Shelf

# SubTask 2: Put Vase2 on CounterTop2.
    Skills Required: GoToObject, PickupObject, GoToObject, PutObject
    Related Objects: vase2(Location=shelf), countertop2(Location=floor)

# Task Put all the vases on the countertop is done.
# Parallel structure: SubTask 1 || SubTask 2