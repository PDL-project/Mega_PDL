# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding KeyChain
#2. Robot not at KeyChain location

# SubTask 1: Store the KeyChain.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: keychain(Location=sofa), sidetable1(Location=floor)

# Initial condition:
#1. Robot not holding Pen
#2. Robot not at Pen location

# SubTask 2: Store the Pen.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: pen(Location=sofa), sidetable2(Location=floor)

# Initial condition:
#1. Robot not holding Pencil
#2. Robot not at Pencil location

# SubTask 3: Store the Pencil.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: pencil(Location=sofa), sidetable3(Location=floor)

# Initial condition:
#1. Robot not holding Pillow
#2. Robot not at Pillow location

# SubTask 4: Store the Pillow.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: pillow(Location=sofa), sofa(Location=floor)

# Task Clear the couch by storing the items in their appropriate positions is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4