# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not at faucet location.
# 2. Faucet is initially on.

# SubTask 1: Turn off the Faucet.
    Skills Required: GoToObject, SwitchOff
    Related Objects: faucet(Location=floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not at light switch location.
# 2. Light is initially on.

# SubTask 2: Turn off the Light.
    Skills Required: GoToObject, SwitchOff
    Related Objects: lightSwitch(Location=floor)

# Task Turn off the faucet and light if either is on is done.
# Parallel structure: SubTask 1 || SubTask 2 (faucet ≠ lightSwitch → no dependency between SubTask 1 and SubTask 2)