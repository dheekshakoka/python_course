print("Welcome to Holiday Planner")

print()
 
print("Step 1: Pick your holiday type")
print("1 - Beach Holiday")
print("2 - Mountain Holiday")
print()
 
choice = int(input("Enter 1 or 2:"))

if choice == 1:
    print("Step 2: Pick your beach activity")
    print("1 - Swimming")
    print("2 - Sandcastle Building")
 
    beach_activity = int(input("Enter 1 or 2:"))

    if beach_activity == 1:
        print("You picked  : Swimming")
        print("Best time   : Morning")
    else:
        print("You picked  : Sandcastle Building")
        print("Best time   : Evening")

elif choice == 2:
    print("Step 2: Pick your mountain activity")
    print("1 - Hiking")
    print("2 - Camping")

    mountain_activity = int(input("Enter 1 or 2: "))

 
    if mountain_activity == 1:
        print("You picked  : Hiking")
        print("Best for    : Exploring trails")
    else:
        print("You picked  : Camping")
        print("Best for    : Staying close to nature")
 
else:
    print("That was not a choice.")
    print("Please enter 1 for Beach Holiday or 2 for Mountain Holiday.")

print("😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀")
print("   Your holiday plan is ready!      ")
print("😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀")