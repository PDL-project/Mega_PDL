# GENERAL TASK DECOMPOSITION 
# Decompose and parallel subtasks where ever possible.

# Initial Precondition analysis:
# 1. KeyChain is on the Sofa.
# 2. Pen is on the Sofa.
# 3. Pencil is on the Sofa.
# 4. Pillow is on the Sofa.

# SubTask 1: Move the KeyChain to its appropriate position.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: KeyChain(Location=Sofa), SideTable(Location=Floor)

# SubTask 2: Move the Pen to its appropriate position.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pen(Location=Sofa), SideTable(Location=Floor)

# SubTask 3: Move the Pencil to its appropriate position.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pencil(Location=Sofa), SideTable(Location=Floor)

# SubTask 4: Move the Pillow to its appropriate position.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pillow(Location=Sofa), Sofa(Location=Floor)

# Task Clear the couch by storing the items in their appropriate positions is done.