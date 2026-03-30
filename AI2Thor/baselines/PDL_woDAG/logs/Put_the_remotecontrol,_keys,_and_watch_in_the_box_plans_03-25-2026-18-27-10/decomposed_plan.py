# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# One box available → all items must be placed sequentially in the same box.

# Initial condition:
#1. Robot not holding RemoteControl
#2. Box is on the Floor

# SubTask 1: Put the RemoteControl in the Box.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: RemoteControl(Location=SideTable), Box(Location=Floor)

# Initial condition:
#1. Robot not holding KeyChain
#2. Box is on the Floor  ← same instance as SubTask 1 → sequential within this group

# SubTask 2: Put the KeyChain in the Box.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: KeyChain(Location=SideTable), Box(Location=Floor)

# Initial condition:
#1. Robot not holding Watch
#2. Box is on the Floor  ← same instance as SubTask 1 and SubTask 2 → sequential within this group

# SubTask 3: Put the Watch in the Box.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Watch(Location=SideTable), Box(Location=Floor)

# Task Put the remotecontrol, keys, and watch in the box is done.
# Sequential structure: SubTask 1 → SubTask 2 → SubTask 3