chores = ["Make your bed", "Feed the pet", "Take out trash"]
remaining = len(chores)  # 2
index = 0

print("You have", remaining, "chores left to do.")

while remaining > 0:
    answer = input(f"Did you finish, {chores[index]}? (yes/no): ")

    if answer == "yes":
        remaining -= 1  # 2 - 1 = 1
        index += 1   # 1
        print("Great")
    else:

        print("Please finish this chore first")

    print(f"Chores remaining: {remaining}")

print("All chores are done!")