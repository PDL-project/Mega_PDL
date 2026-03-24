# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Different tables available → distribute items across different tables for parallel execution.

# PARALLEL GROUP A — CoffeeTable
# Initial condition:
#1. Robot not holding Vase
#2. CoffeeTable is available

# SubTask 1: Put the Vase on the CoffeeTable.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: vase(Location=SideTable1), coffeeTable(Location=Floor)

# PARALLEL GROUP B — TVStand
# Initial condition:
#1. Robot not holding TissueBox
#2. TVStand is available

# SubTask 2: Put the TissueBox on the TVStand.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: tissueBox(Location=TVStand), tvStand(Location=Floor)

# PARALLEL GROUP C — SideTable2
# Initial condition:
#1. Robot not holding RemoteControl
#2. SideTable2 is available

# SubTask 3: Put the RemoteControl on the SideTable2.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: remoteControl(Location=SideTable2), sideTable2(Location=Floor)

# Task Put the vase, tissue box, and remote control on the table is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3