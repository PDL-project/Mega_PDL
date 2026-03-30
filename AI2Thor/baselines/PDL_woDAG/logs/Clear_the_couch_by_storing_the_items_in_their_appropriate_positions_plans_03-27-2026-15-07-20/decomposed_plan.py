# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding KeyChain
#2. Sofa is the initial location of KeyChain

# SubTask 1: Store the KeyChain on the SideTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: keychain(Location=sofa), sidetable1(Location=floor)

# Initial condition:
#1. Robot not holding Pen
#2. Sofa is the initial location of Pen

# SubTask 2: Store the Pen on the SideTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: pen(Location=sofa), sidetable2(Location=floor)

# Initial condition:
#1. Robot not holding Pencil
#2. Sofa is the initial location of Pencil

# SubTask 3: Store the Pencil on the SideTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: pencil(Location=sofa), sidetable3(Location=floor)

# Initial condition:
#1. Robot not holding Pillow
#2. Sofa is the initial location of Pillow

# SubTask 4: Store the Pillow on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: pillow(Location=sofa), sofa(Location=floor)

# Task Clear the couch by storing the items in their appropriate positions is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4