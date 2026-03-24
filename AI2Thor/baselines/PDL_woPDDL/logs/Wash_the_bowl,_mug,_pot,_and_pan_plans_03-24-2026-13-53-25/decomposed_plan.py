# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Multiple objects to wash → distribute tasks across different instances of the sink for parallel execution.

# PARALLEL GROUP A — Sink
# Initial condition:
#1. Robot not holding Bowl
#2. Robot not at Bowl location

# SubTask 1: Wash the Bowl.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: bowl(Location=counterTop), sink(Location=floor)

# PARALLEL GROUP B — Sink (runs concurrently with Group A)
# Initial condition:
#1. Robot not holding Mug
#2. Robot not at Mug location

# SubTask 2: Wash the Mug.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: mug(Location=counterTop), sink(Location=floor)

# PARALLEL GROUP C — Sink (runs concurrently with Group A and B)
# Initial condition:
#1. Robot not holding Pot
#2. Robot not at Pot location

# SubTask 3: Wash the Pot.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: pot(Location=counterTop), sink(Location=floor)

# PARALLEL GROUP D — Sink (runs concurrently with Group A, B, and C)
# Initial condition:
#1. Robot not holding Pan
#2. Robot not at Pan location

# SubTask 4: Wash the Pan.
    Skills Required: GoToObject, PickupObject, CleanObject, PutObject
    Related Objects: pan(Location=counterTop), sink(Location=floor)

# Task Wash the bowl, mug, pot, and pan is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4