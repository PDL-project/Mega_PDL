# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Objects on the table: Book, Newspaper, Pen, Pencil, Plate
# Target location: Sofa

# PARALLEL GROUP A — Move items from DiningTable to Sofa
# Initial condition:
#1. Robot not holding Book
#2. Book is on the DiningTable

# SubTask 1: Move the Book to the Sofa.
    Skills Required: GoToObject, PickupObject, GoToObject, PutObject
    Related Objects: Book(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Newspaper
#2. Newspaper is on the DiningTable

# SubTask 2: Move the Newspaper to the Sofa.
    Skills Required: GoToObject, PickupObject, GoToObject, PutObject
    Related Objects: Newspaper(Location=DiningTable), Sofa(Location=Floor)

# PARALLEL GROUP B — Move items from DiningTable to Sofa
# Initial condition:
#1. Robot not holding Pen
#2. Pen is on the DiningTable

# SubTask 3: Move the Pen to the Sofa.
    Skills Required: GoToObject, PickupObject, GoToObject, PutObject
    Related Objects: Pen(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Pencil
#2. Pencil is on the DiningTable

# SubTask 4: Move the Pencil to the Sofa.
    Skills Required: GoToObject, PickupObject, GoToObject, PutObject
    Related Objects: Pencil(Location=DiningTable), Sofa(Location=Floor)

# Initial condition:
#1. Robot not holding Plate
#2. Plate is on the DiningTable

# SubTask 5: Move the Plate to the Sofa.
    Skills Required: GoToObject, PickupObject, GoToObject, PutObject
    Related Objects: Plate(Location=DiningTable), Sofa(Location=Floor)

# Task Move everything on the table to the sofa is done.
# Parallel structure: [SubTask 1 || SubTask 2] || [SubTask 3 || SubTask 4] || SubTask 5