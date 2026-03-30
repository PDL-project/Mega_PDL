# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding bowl
#2. Robot not at bowl location

# SubTask 1: Wash the Bowl.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: bowl(Location=counterTop), sink(Location=floor)

# Initial condition:
#1. Robot not holding mug
#2. Robot not at mug location

# SubTask 2: Wash the Mug.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: mug(Location=counterTop), sink(Location=floor)

# Initial condition:
#1. Robot not holding pot
#2. Robot not at pot location

# SubTask 3: Wash the Pot.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: pot(Location=counterTop), sink(Location=floor)

# Initial condition:
#1. Robot not holding pan
#2. Robot not at pan location

# SubTask 4: Wash the Pan.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: pan(Location=counterTop), sink(Location=floor)

# Task Wash the bowl, mug, pot, and pan is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4