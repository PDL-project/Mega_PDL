# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding Vase
#2. Robot not at Vase location

# SubTask 1: Put the Vase on the CoffeeTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: vase(Location=SideTable1), coffeeTable(Location=Floor)

# Initial condition:
#1. Robot not holding TissueBox
#2. Robot not at TissueBox location

# SubTask 2: Put the TissueBox on the CoffeeTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: tissueBox(Location=TVStand), coffeeTable(Location=Floor)

# Initial condition:
#1. Robot not holding RemoteControl
#2. Robot not at RemoteControl location

# SubTask 3: Put the RemoteControl on the CoffeeTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: remoteControl(Location=SideTable2), coffeeTable(Location=Floor)

# Task Put the vase, tissue box, and remote control on the table is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3