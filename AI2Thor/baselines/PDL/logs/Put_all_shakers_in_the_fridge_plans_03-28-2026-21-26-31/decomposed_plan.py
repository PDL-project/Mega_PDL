# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding SaltShaker
#2. Fridge is initially closed

# SubTask 1: Put the SaltShaker in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: saltShaker(Location=counterTop), fridge(Location=floor)

# Initial condition:
#1. Robot not holding PepperShaker
#2. Fridge is initially closed  ← same instance as SubTask 1 → sequential within this group

# SubTask 2: Put the PepperShaker in the Fridge.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObjectInFridge, CloseObject
    Related Objects: pepperShaker(Location=counterTop), fridge(Location=floor)

# Task Put all shakers in the fridge is done.
# Sequential structure: SubTask 1 → SubTask 2 (same fridge instance → must run sequentially)