# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Multiple cabinets available → distribute tasks across different cabinets for parallel execution.

# PARALLEL GROUP A — Cabinet1
# Initial condition:
#1. Cabinet1 is open

# SubTask 1: Close Cabinet1.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet1(Location=floor)

# PARALLEL GROUP B — Cabinet2
# Initial condition:
#1. Cabinet2 is open

# SubTask 2: Close Cabinet2.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet2(Location=floor)

# PARALLEL GROUP C — Cabinet3
# Initial condition:
#1. Cabinet3 is open

# SubTask 3: Close Cabinet3.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet3(Location=floor)

# PARALLEL GROUP D — Cabinet4
# Initial condition:
#1. Cabinet4 is open

# SubTask 4: Close Cabinet4.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet4(Location=floor)

# PARALLEL GROUP E — Cabinet5
# Initial condition:
#1. Cabinet5 is open

# SubTask 5: Close Cabinet5.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet5(Location=floor)

# PARALLEL GROUP F — Cabinet6
# Initial condition:
#1. Cabinet6 is open

# SubTask 6: Close Cabinet6.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet6(Location=floor)

# PARALLEL GROUP G — Cabinet7
# Initial condition:
#1. Cabinet7 is open

# SubTask 7: Close Cabinet7.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet7(Location=floor)

# PARALLEL GROUP H — Cabinet8
# Initial condition:
#1. Cabinet8 is open

# SubTask 8: Close Cabinet8.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet8(Location=floor)

# PARALLEL GROUP I — Cabinet9
# Initial condition:
#1. Cabinet9 is open

# SubTask 9: Close Cabinet9.
    Skills Required: GoToObject, CloseObject
    Related Objects: cabinet9(Location=floor)

# Task Close all the cabinets is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5 || SubTask 6 || SubTask 7 || SubTask 8 || SubTask 9