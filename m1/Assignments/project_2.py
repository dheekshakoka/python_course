import keyword

name = input("Enter your name:")
goal = input("Enter one personal goal: ")
target_month = input("Enter your target month: ")

print("Personal Goals")
print("Your name is:", name)
print("Your goal is:", goal)
print("Your target month is:", target_month)
print("get your goal done by", target_month)
print(f"\nYour need to reach this goal: {goal}\n")
print("Python keywords:")
print(keyword.kwlist)