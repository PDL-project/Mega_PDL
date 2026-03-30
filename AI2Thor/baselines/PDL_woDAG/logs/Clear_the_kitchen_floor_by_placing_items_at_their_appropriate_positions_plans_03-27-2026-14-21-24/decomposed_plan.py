# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
# 1. Robot not holding Apple
# 2. Apple is on the Floor

# SubTask 1: Place the Apple on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: apple(Location=floor), countertop1(Location=floor)

# Initial condition:
# 1. Robot not holding Tomato
# 2. Tomato is on the Floor

# SubTask 2: Place the Tomato on the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: tomato(Location=floor), countertop2(Location=floor)

# Task Clear the kitchen floor by placing items at their appropriate positions is done.
# Parallel structure: SubTask 1 || SubTask 2