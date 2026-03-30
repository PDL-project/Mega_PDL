# GENERAL TASK DECOMPOSITION
# Decompose and parallelize subtasks where ever possible
# Independent subtasks:

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Apple.
# 2. Robot not at Apple location.

# SubTask 1: Move the Apple to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: apple(Location=CounterTop), CounterTop1(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Bread.
# 2. Robot not at Bread location.

# SubTask 2: Move the Bread to the Sink.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: bread(Location=CounterTop), Sink(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding ButterKnife.
# 2. Robot not at ButterKnife location.

# SubTask 3: Move the ButterKnife to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: butterKnife(Location=CounterTop), CounterTop2(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Fork.
# 2. Robot not at Fork location.

# SubTask 4: Move the Fork to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: fork(Location=CounterTop), CounterTop3(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Lettuce.
# 2. Robot not at Lettuce location.

# SubTask 5: Move the Lettuce to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: lettuce(Location=CounterTop), CounterTop1(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Mug.
# 2. Robot not at Mug location.

# SubTask 6: Move the Mug to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: mug(Location=CounterTop), CounterTop2(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding PaperTowelRoll.
# 2. Robot not at PaperTowelRoll location.

# SubTask 7: Move the PaperTowelRoll to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: paperTowelRoll(Location=CounterTop), CounterTop3(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding PepperShaker.
# 2. Robot not at PepperShaker location.

# SubTask 8: Move the PepperShaker to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: pepperShaker(Location=CounterTop), CounterTop1(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding SaltShaker.
# 2. Robot not at SaltShaker location.

# SubTask 9: Move the SaltShaker to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: saltShaker(Location=CounterTop), CounterTop2(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding SoapBottle.
# 2. Robot not at SoapBottle location.

# SubTask 10: Move the SoapBottle to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: soapBottle(Location=CounterTop), CounterTop3(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Spatula.
# 2. Robot not at Spatula location.

# SubTask 11: Move the Spatula to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: spatula(Location=CounterTop), CounterTop1(Location=Floor)

# Initial Precondition analyze due to previous subtask:
# 1. Robot not holding Tomato.
# 2. Robot not at Tomato location.

# SubTask 12: Move the Tomato to the CounterTop.
    Skills Required: GoToObject, PickupObject, PutObject
    Related Objects: tomato(Location=CounterTop), CounterTop2(Location=Floor)

# Task Clear the central countertop by placing items in their appropriate positions is done.
# Parallel structure: [SubTask 1 || SubTask 2 || SubTask 3 || SubTask 4 || SubTask 5 || SubTask 6 || SubTask 7 || SubTask 8 || SubTask 9 || SubTask 10 || SubTask 11 || SubTask 12]