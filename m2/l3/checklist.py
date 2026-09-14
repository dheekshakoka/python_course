"""
OUTPUT:

You have 4 chores to finish today!

Did you finish Make your bed? (yes/no): no
Finish it first!
Chores remaining: 4

Did you finish Make your bed? (yes/no): yes
Great job!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): yes
Great job!
Chores remaining: 2

Did you finish Take out the trash? (yes/no): yes
Great job!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): no
Finish it first!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): no
Finish it first!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): yes
Great job!
Chores remaining: 0

All chores are complete!
"""

# List of chores to complete
chores = ["Make your bed", "Feed the pet", "Take out the trash", "Wash the dishes"]

chore_1 = input("Did you make your bed?")
while chore_1 == "no":
    chore_1 = input("Did you make your bed?")
    if chore_1 == "yes":
        break
print("Chores remaining: 3")

chore_2 = input("Did you feed the pet?")
while chore_2 == "no":
    chore_2 = input("Did you feed the pet?")
    if chore_2 == "yes":
        break
print("Chores remaining: 2")

chore_3 = input("Did you take out the trash?")
while chore_3 == "no":
    chore_3 = input("Did you take out the trash?")
    if chore_3 == "yes":
        break
print("Chores remaining: 1")

chore_4 = input("Did you wash the dishes?")
while chore_4 == "no":
    chore_4 = input("Did you wash the dishes?")
    if chore_4 == "yes":
        break
print("You are done!")
        