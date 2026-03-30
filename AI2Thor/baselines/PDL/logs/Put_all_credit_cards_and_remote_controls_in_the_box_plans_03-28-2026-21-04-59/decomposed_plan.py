# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding CreditCard
#2. Box is available

# SubTask 1: Put the CreditCard in the Box.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: CreditCard(Location=Chair), Box(Location=Floor)

# Initial condition:
#1. Robot not holding RemoteControl
#2. Box is available

# SubTask 2: Put the RemoteControl in the Box.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: RemoteControl(Location=SideTable), Box(Location=Floor)

# Task Put all credit cards and remote controls in the box is done.
# Parallel structure: SubTask 1 || SubTask 2