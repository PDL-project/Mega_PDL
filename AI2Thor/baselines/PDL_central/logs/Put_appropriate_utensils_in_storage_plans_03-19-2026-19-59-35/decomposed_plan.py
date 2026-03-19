# GENERAL TASK DECOMPOSITION 
Decompose and parallel subtasks wherever possible.

# Initial Precondition analysis:
1. Robot not holding any utensils.
2. Robot not at utensil locations.

# SubTask 1: Store the Fork.
   Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   Related Objects: fork(Location=counterTop), drawer(Location=floor)

# Initial Precondition analysis due to previous subtask:
1. Robot not holding spoon.
2. Robot not at spoon location.
3. Drawer is initially closed.

# SubTask 2: Store the Spoon.
   Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   Related Objects: spoon(Location=counterTop), drawer(Location=floor)

# Initial Precondition analysis due to previous subtask:
1. Robot not holding knife.
2. Robot not at knife location.
3. Drawer is initially closed.

# SubTask 3: Store the Knife.
   Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   Related Objects: knife(Location=counterTop), drawer(Location=floor)

# Initial Precondition analysis due to previous subtask:
1. Robot not holding ladle.
2. Robot not at ladle location.
3. Drawer is initially closed.

# SubTask 4: Store the Ladle.
   Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   Related Objects: ladle(Location=counterTop), drawer(Location=floor)

# Initial Precondition analysis due to previous subtask:
1. Robot not holding spatula.
2. Robot not at spatula location.
3. Drawer is initially closed.

# SubTask 5: Store the Spatula.
   Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   Related Objects: spatula(Location=counterTop), drawer(Location=floor)

# Task Put appropriate utensils in storage is done.