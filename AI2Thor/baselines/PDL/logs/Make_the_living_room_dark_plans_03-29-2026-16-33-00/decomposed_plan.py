# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
# 1. Curtains are open
# 2. LightSwitch is on
# 3. FloorLamp is on
# 4. DeskLamp is on

# SubTask 1: Close the Curtains.
    Skills Required: GoToObject, CloseObject
    Related Objects: Curtains(Location=Floor)

# SubTask 2: Switch off the LightSwitch.
    Skills Required: GoToObject, SwitchOff
    Related Objects: LightSwitch(Location=Floor)

# SubTask 3: Switch off the FloorLamp.
    Skills Required: GoToObject, SwitchOff
    Related Objects: FloorLamp(Location=Floor)

# SubTask 4: Switch off the DeskLamp.
    Skills Required: GoToObject, SwitchOff
    Related Objects: DeskLamp(Location=SideTable)

# Task Make the living room dark is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4