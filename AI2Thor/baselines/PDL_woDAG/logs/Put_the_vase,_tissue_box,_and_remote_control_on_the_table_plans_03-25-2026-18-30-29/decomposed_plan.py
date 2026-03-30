# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding Vase
#2. CoffeeTable is available

# SubTask 1: Put the Vase on the CoffeeTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Vase(Location=SideTable1), CoffeeTable(Location=Floor)

# Initial condition:
#1. Robot not holding TissueBox
#2. CoffeeTable is available

# SubTask 2: Put the TissueBox on the CoffeeTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: TissueBox(Location=TVStand), CoffeeTable(Location=Floor)

# Initial condition:
#1. Robot not holding RemoteControl
#2. CoffeeTable is available

# SubTask 3: Put the RemoteControl on the CoffeeTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: RemoteControl(Location=SideTable2), CoffeeTable(Location=Floor)

# Task Put the vase, tissue box, and remote control on the table is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3