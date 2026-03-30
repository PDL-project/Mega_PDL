# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Only one box available → all items must be placed in the same box sequentially.

# Initial condition:
#1. Robot not holding CreditCard
#2. Box is open

# SubTask 1: Put the CreditCard in the Box.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: CreditCard(Location=DiningTable), Box(Location=Floor)

# Initial condition:
#1. Robot not holding RemoteControl
#2. Box is open  ← same instance as SubTask 1 → sequential within this group

# SubTask 2: Put the RemoteControl in the Box.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: RemoteControl(Location=SideTable), Box(Location=Floor)

# Task Put all credit cards and remote controls in the box is done.
# Sequential structure: SubTask 1 → SubTask 2