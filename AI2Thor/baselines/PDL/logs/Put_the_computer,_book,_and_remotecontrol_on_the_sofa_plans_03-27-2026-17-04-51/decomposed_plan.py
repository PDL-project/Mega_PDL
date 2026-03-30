# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# PARALLEL GROUP A — Sofa
# Initial condition:
#1. Robot not holding Laptop
#2. Sofa is available

# SubTask 1: Put the Laptop on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Laptop(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Book
#2. Sofa is available  ← same instance as SubTask 1 → sequential within this group

# SubTask 2: Put the Book on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Book(Location=Chair), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding RemoteControl
#2. Sofa is available  ← same instance as SubTask 1 and SubTask 2 → sequential within this group

# SubTask 3: Put the RemoteControl on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: RemoteControl(Location=SideTable), Sofa(Location=Floor)

# Task Put the computer, book, and remotecontrol on the sofa is done.
# Parallel structure: SubTask 1 → SubTask 2 → SubTask 3