# GENERAL TASK DECOMPOSITION 
Decompose and parallel subtasks where ever possible.

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at the location of any object on the couch.

# SubTask 1: Move the KeyChain from the Sofa to the SideTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: KeyChain(Location=Sofa), SideTable(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at the location of any object on the couch.

# SubTask 2: Move the Pen from the Sofa to the SideTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pen(Location=Sofa), SideTable(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at the location of any object on the couch.

# SubTask 3: Move the Pencil from the Sofa to the SideTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pencil(Location=Sofa), SideTable(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding any object.
# 2. Robot not at the location of any object on the couch.

# SubTask 4: Move the Pillow from the Sofa to the ArmChair.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pillow(Location=Sofa), ArmChair(Location=Floor)

# Task Clear the couch by storing the items in their appropriate positions is done.