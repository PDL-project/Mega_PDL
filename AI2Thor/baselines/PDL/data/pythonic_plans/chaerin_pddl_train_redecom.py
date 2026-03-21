# GENERAL TASK DECOMPOSITION
# Decompose and parallel subtasks where ever possible
# Independent subtasks:

# INSTANCE NAMING RULE (applies to redecomposition too):
# When multiple instances of the same receptacle type exist (e.g., Drawer1 and Drawer2, Fridge1 and Fridge2),
# assign DIFFERENT instances to different subtasks to maximize parallel execution.
# If the originally assigned instance is full/blocked/unavailable, redirect to a DIFFERENT instance
# and check whether that enables parallel execution with other subtasks.


## Case 1 (example):
# Failure Reason
Robot1 is already holding pen|01.20. Robot1 cannot pick up Spoon|02.15 while its gripper is occupied.
pen can not put in drawer1. because it is already full. place another drawer.

# Action Plan
To resolve the failure, the highest priority is to clear the robot's gripper.
The robot will first complete the original goal of "placing the pen in drawer2" to free up the gripper, then retry the interrupted task of "picking up the spoon." Subsequently, it will proceed sequentially with the remaining tasks: placing the doll into the box.
Since drawer1 is full, pen is redirected to drawer2. Check if other subtasks also use drawer2 — if not, no new dependency is introduced.

# Redecomposition of Subtasks

### Initial Condition Analysis (Based on Already Achieved Effects):
1. Robot1 is at the fridge.
2. Robot1 is holding pen.
3. Drawer1 is already full → pen redirected to Drawer2.

### SubTask 1: Place the pen in Drawer2.
   Skills Required: GoToObject, PutObject
   Related Objects: pen(Location=robot1), drawer2(Location=cabinet)

   - Preconditions: holding(robot1, pen), at(robot1, drawer2)
   - Effects: at-location(pen, drawer2), not holding(robot1, pen), hand-empty(robot1)

### SubTask 2: Put the Spoon in the Box.
   Skills Required: GoToObject, PickUp, PutObject
   Related Objects: spoon(Location=diningTable), box(Location=kitchen)

   - Preconditions: hand-empty(robot1)
   - Effects: in-box(spoon, box), hand-empty(robot1)

### SubTask 3: Put doll in the Box.
   Skills Required: GoToObject, PickUp, PutObject
   Related Objects: doll(Location=diningTable), box(Location=kitchen)

   - Preconditions: hand-empty(robot1)
   - Effects: in-box(doll, box), hand-empty(robot1)

## Case 1 (example) done.


## Case 2 (example):
# Failure Reason
Toybox|05.12 is not an Openable object (Locked or Fixed). The action Open(robot1, toybox) is physically impossible.

# Action Plan
Since the failure is classified as Category A (Physically Impossible), the subtask of opening the toyBox will be dropped.
However, the remaining tasks that do not depend on opening this specific box remain valid. The robot will skip the problematic subtask and proceed with the next available independent tasks: placing the block on the shelf and putting the ball in the basket.

# Redecomposition of Subtasks

### Initial Condition Analysis (Based on Already Achieved Effects):
1. Robot1 is at the play_zone.
2. Robot1 is hand-empty.
3. Drawer1 is already full.

### SubTask 1: Place the Block on the Shelf.
   Skills Required: GoToObject, PickUp, PutObject
   Related Objects: block(Location=floor), shelf(Location=corner)

   - Preconditions: hand-empty(robot1), at(robot1, play_zone)
   - Effects: at-location(block, shelf), hand-empty(robot1)

### SubTask 2: Put the Ball in Drawer2.
   Skills Required: GoToObject, PickUp, PutObject
   Related Objects: ball(Location=floor), drawer2(Location=living_room)

   - Preconditions: hand-empty(robot1)
   - Effects: in-drawer(ball, drawer2), hand-empty(robot1)

## Case 2 (example) done.


## Case 3 (example):
# Failure Reason
Fridge1|-00.97 is already full. Cannot place Tomato inside Fridge1.
Robot2 is currently placing Lettuce in Fridge1 (resource conflict).

# Action Plan
Since Fridge1 is full and occupied, redirect Tomato to Fridge2.
Fridge2 is a different instance → no resource conflict with the Fridge1 subtasks.
This redirection also enables parallel execution: Robot1 can use Fridge2 simultaneously while Robot2 finishes with Fridge1.

# Redecomposition of Subtasks

### Initial Condition Analysis (Based on Already Achieved Effects):
1. Robot1 completed: Bread is in Fridge1.
2. Robot2 is currently executing: Lettuce → Fridge1 (in progress).
3. Fridge1 is full → Tomato cannot go into Fridge1.
4. Fridge2 is available and empty.

### SubTask 1 (redirect): Put the Tomato in Fridge2.
   Skills Required: GoToObject, PickupObject, OpenObject, PutObject, CloseObject
   Related Objects: tomato(Location=counterTop), fridge2(Location=floor)

   - Preconditions: hand-empty(robot1), fridge2 is not full
   - Effects: at-location(tomato, fridge2), hand-empty(robot1), fridge2 is closed
   - Note: Uses fridge2 (different instance from fridge1) → can run in parallel with Robot2's Fridge1 subtask.

## Case 3 (example) done.
