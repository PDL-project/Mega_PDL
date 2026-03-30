# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial condition:
#1. Robot not holding Book
#2. Book is on the DiningTable

# SubTask 1: Put the Book on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Book(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Pen
#2. Pen is on the DiningTable

# SubTask 2: Put the Pen on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pen(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Pencil
#2. Pencil is on the CoffeeTable

# SubTask 3: Put the Pencil on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Pencil(Location=CoffeeTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Laptop
#2. Laptop is on the DiningTable

# SubTask 4: Put the Laptop on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Laptop(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Notebook
#2. Notebook is not explicitly listed, but can be represented by Newspaper

# SubTask 5: Put the Newspaper on the Sofa.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: Newspaper(Location=DiningTable), Sofa(Location=Floor)

# Task Put all school supplies in the sofa is done.
# Parallel structure: SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5