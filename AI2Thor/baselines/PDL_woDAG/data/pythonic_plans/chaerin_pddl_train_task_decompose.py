# INSTANCE NAMING RULE:
# When multiple instances of the same receptacle type exist in the scene
# (e.g., Drawer1 and Drawer2, Fridge1 and Fridge2, CounterTop1 and CounterTop2),
# assign DIFFERENT instances to different subtasks to maximize parallel execution.
# Subtasks using DIFFERENT instances have NO resource dependency → can run in parallel.
# Subtasks using the SAME instance have a resource dependency → must run sequentially.

# Task Description: Put the Fork and Spoon in a drawer, and put the Pen and Pencil in another drawer. (Scene objects include: Drawer1, Drawer2, Fork, Spoon, Pen, Pencil)

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Two drawers available → distribute items across Drawer1 and Drawer2 for parallel execution.

# PARALLEL GROUP A — Drawer1
# Initial condition:
#1. Robot not holding Fork
#2. Drawer1 is closed

# SubTask 1: Put the Fork in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: fork(Location=diningTable), drawer1(Location=cabinet)

# Initial condition:
#1. Robot not holding Spoon
#2. Drawer1 is closed  ← same instance as SubTask 1 → sequential within this group

# SubTask 2: Put the Spoon in Drawer1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: spoon(Location=counterTop), drawer1(Location=cabinet)

# PARALLEL GROUP B — Drawer2 (runs concurrently with Group A)
# Initial condition:
#1. Robot not holding Pen
#2. Drawer2 is closed  ← different instance from Drawer1 → no dependency with Group A

# SubTask 3: Put the Pen in Drawer2.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: pen(Location=diningTable), drawer2(Location=cabinet)

# Initial condition:
#1. Robot not holding Pencil
#2. Drawer2 is closed  ← same instance as SubTask 3 → sequential within this group

# SubTask 4: Put the Pencil in Drawer2.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: pencil(Location=counterTop), drawer2(Location=cabinet)

# Task Put the Fork and Spoon in a drawer, and put the Pen and Pencil in another drawer is done.
# Parallel structure: [SubTask 1 → SubTask 2] || [SubTask 3 → SubTask 4]


# Task Description: Put an Egg in the Fridge, and place a pot containing Apple slices into the refrigerator.


# GENERAL TASK DECOMPOSITION
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# Initial condition analyze due to previous subtask:
#1. Robot not at egg location
#2. Robot not holding egg
#3. fridge is fridge, and initally closed

# SubTask 1: Put an Egg in Fridge1.
    Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
    Related Objects: egg(Location=fridge), fridge1(Location=floor)

# Initial condition analyze due to previous subtask:
#1. Robot not at apple location
#2. Robot not holding apple
#3. Robot not holding knife

# SubTask 2: Prepare Apple Slices.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: apple(Location=counterTop), knife(Location=diningTable), pot(Location=stoveBurner)

# Inital condition analyze due to previous subtask:
#1. Robot at pot location
#2. Fridge is Fridge, and initally closed
#3. Robot not holding pot initally.

# SubTask 3: Place the Pot with Apple Slices in Fridge2.
    Skills Required: GoToObject, PickupObject, PutObject, OpenObject, CloseObject
    Related Objects: pot(Location=stoveBurner), apple(Location=counterTop), fridge2(Location=floor)

# Task Put an Egg in the Fridge, and place a pot containing Apple slices into the refrigerator is done.
# Parallel structure: SubTask 1 || [SubTask 2 → SubTask 3]  (fridge1 ≠ fridge2 → no dependency between SubTask 1 and SubTask 3)


# Task Description: Make a sandwich with sliced lettuce, sliced tomato, sliced bread and serve it on a washed plate.

# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding lettuce.
# 2. Robot not at lettuce location.

# SubTask 1: Slice the Lettuce.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=diningTable), lettuce(Location=diningTable)

# Initial Precondition analyze due to previous subtask:
#1. Robot not holding tomate
#2. Robot not at tomate location
#3. Robot not holding knife

# SubTask 2: Slice the Tomato.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=diningTable), tomato(Location=counterTop)

#1. Robot not holding bread
#2. Robot not at  bread location.

# SubTask 3: Slice the Bread.
    Skills Required: GoToObject, PickupObject, SliceObject, PutObject
    Related Objects: knife(Location=diningTable), bread(Location=diningTable)

#1. Robot not holding plate
#2. Robot not at plate location

# SubTask 4: Wash the Plate.
    Skills Required: GoToObject, PickupObject, PutObject, SwitchOn, SwitchOff
    Related Object: plate(Location=counterTop), sink(Location=floor)

#1. Robot not holding bread, lettuce, or tomato
#2. Robot holding plate
#3. Robot not at bread, lettuce, or tomato location

# SubTask 5: Assemble the Sandwich.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Object: plate1(Location=counterTop), bread(Location=diningTable), lettuce(Location=diningTable), tomato(Location=counterTop)

# Task Make a sandwich with sliced lettuce, sliced tomato, sliced bread and serve it on a washed plate is done.
