# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
# 1. Robot not at StoveKnob1 location

# SubTask 1: Turn on StoveKnob1.
    Skills Required: GoToObject, SwitchOn
    Related Objects: stoveKnob1(Location=floor)

# Initial condition:
# 1. Robot not at StoveKnob2 location

# SubTask 2: Turn on StoveKnob2.
    Skills Required: GoToObject, SwitchOn
    Related Objects: stoveKnob2(Location=floor)

# Initial condition:
# 1. Robot not at StoveKnob3 location

# SubTask 3: Turn on StoveKnob3.
    Skills Required: GoToObject, SwitchOn
    Related Objects: stoveKnob3(Location=floor)

# Initial condition:
# 1. Robot not at StoveKnob4 location

# SubTask 4: Turn on StoveKnob4.
    Skills Required: GoToObject, SwitchOn
    Related Objects: stoveKnob4(Location=floor)

# Task Turn on all the stove knobs is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4