# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Curtains are open
#2. Robot not at curtains location

# SubTask 1: Close the Curtains.
    Skills Required: GoToObject, CloseObject
    Related Objects: Curtains(Location=Floor)

# Initial condition:
#1. LightSwitch is on
#2. Robot not at LightSwitch location

# SubTask 2: Switch off the Light.
    Skills Required: GoToObject, SwitchOff
    Related Objects: LightSwitch(Location=Floor)

# Task Make the living room dark is done.
# Parallel structure: SubTask 1 || SubTask 2