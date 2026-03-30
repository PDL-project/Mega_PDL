# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding Book
#2. Robot not at Book location

# SubTask 1: Put the Book on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Book(Location=Chair), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Pen
#2. Robot not at Pen location

# SubTask 2: Put the Pen on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pen(Location=Chair), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Pencil
#2. Robot not at Pencil location

# SubTask 3: Put the Pencil on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pencil(Location=CoffeeTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Laptop
#2. Robot not at Laptop location

# SubTask 4: Put the Laptop on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Laptop(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding CreditCard
#2. Robot not at CreditCard location

# SubTask 5: Put the CreditCard on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: CreditCard(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Watch
#2. Robot not at Watch location

# SubTask 6: Put the Watch on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Watch(Location=SideTable), Sofa(Location=Floor)

# Task Put all school supplies in the sofa is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5 || SubTask 6