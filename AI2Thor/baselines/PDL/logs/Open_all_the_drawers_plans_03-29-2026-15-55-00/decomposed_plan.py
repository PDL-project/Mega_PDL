# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks: Each drawer can be opened independently.

# Initial condition:
#1. Drawer1 is closed

# SubTask 1: Open Drawer1.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer1(Location=floor)

# Initial condition:
#1. Drawer2 is closed

# SubTask 2: Open Drawer2.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer2(Location=floor)

# Initial condition:
#1. Drawer3 is closed

# SubTask 3: Open Drawer3.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer3(Location=floor)

# Initial condition:
#1. Drawer4 is closed

# SubTask 4: Open Drawer4.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer4(Location=floor)

# Initial condition:
#1. Drawer5 is closed

# SubTask 5: Open Drawer5.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer5(Location=floor)

# Initial condition:
#1. Drawer6 is closed

# SubTask 6: Open Drawer6.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer6(Location=floor)

# Initial condition:
#1. Drawer7 is closed

# SubTask 7: Open Drawer7.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer7(Location=floor)

# Initial condition:
#1. Drawer8 is closed

# SubTask 8: Open Drawer8.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer8(Location=floor)

# Initial condition:
#1. Drawer9 is closed

# SubTask 9: Open Drawer9.
    Skills Required: GoToObject, OpenObject
    Related Objects: drawer9(Location=floor)

# Task Open all the drawers is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5 || SubTask 6 || SubTask 7 || SubTask 8 || SubTask 9