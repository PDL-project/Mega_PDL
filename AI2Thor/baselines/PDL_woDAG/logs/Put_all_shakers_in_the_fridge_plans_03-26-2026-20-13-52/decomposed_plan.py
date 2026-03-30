# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding SaltShaker.
# 2. Robot not at SaltShaker location.
# 3. Fridge is initially closed.

# SubTask 1: Put the SaltShaker in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: saltShaker(Location=counterTop), fridge(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding PepperShaker.
# 2. Robot not at PepperShaker location.
# 3. Fridge is initially closed.

# SubTask 2: Put the PepperShaker in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: pepperShaker(Location=counterTop), fridge(Location=floor)

# Task Put all shakers in the fridge is done.
# Parallel structure: SubTask 1 || SubTask 2