# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Multiple cabinets available → distribute actions across different cabinets for parallel execution.

# PARALLEL GROUP A — Cabinets on Floor Level
# Initial condition:
#1. Robot not at Cabinet1 location
#2. Cabinet1 is open

# SubTask 1: Close Cabinet1.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet1(Location=floor)

# Initial condition:
#1. Robot not at Cabinet2 location
#2. Cabinet2 is open

# SubTask 2: Close Cabinet2.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet2(Location=floor)

# Initial condition:
#1. Robot not at Cabinet3 location
#2. Cabinet3 is open

# SubTask 3: Close Cabinet3.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet3(Location=floor)

# Initial condition:
#1. Robot not at Cabinet7 location
#2. Cabinet7 is open

# SubTask 4: Close Cabinet7.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet7(Location=floor)

# PARALLEL GROUP B — Cabinets on Upper Level
# Initial condition:
#1. Robot not at Cabinet4 location
#2. Cabinet4 is open

# SubTask 5: Close Cabinet4.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet4(Location=floor)

# Initial condition:
#1. Robot not at Cabinet5 location
#2. Cabinet5 is open

# SubTask 6: Close Cabinet5.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet5(Location=floor)

# Initial condition:
#1. Robot not at Cabinet6 location
#2. Cabinet6 is open

# SubTask 7: Close Cabinet6.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet6(Location=floor)

# Initial condition:
#1. Robot not at Cabinet8 location
#2. Cabinet8 is open

# SubTask 8: Close Cabinet8.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet8(Location=floor)

# Initial condition:
#1. Robot not at Cabinet9 location
#2. Cabinet9 is open

# SubTask 9: Close Cabinet9.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet9(Location=floor)

# Task Close all the cabinets is done.
# Parallel structure: [SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4] || [SubTask 5 || SubTask 6 || SubTask 7 || SubTask 8 || SubTask 9]