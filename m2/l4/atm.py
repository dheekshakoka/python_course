"""
OUTPUT:
=== ATM Cash Dispenser ===

Enter customer name: Ajay
Enter withdrawal amount: 100

Dispensing 100 units:

1 x 100 note(s)
Transaction complete!


Serve another customer? (yes/no): yes
Enter customer name: Rahul
Enter withdrawal amount: 125

Dispensing 125 units:

1 x 100 note(s)
1 x 20 note(s)
1 x 5 note(s)
Transaction complete!


Serve another customer? (yes/no): yes
Enter customer name: Chethan
Enter withdrawal amount: 107

Dispensing 107 units:

1 x 100 note(s)
1 x 5 note(s)
2 x 1 note(s)
Transaction complete!


Serve another customer? (yes/no): no

Customers Served : 3
Total Amount Dispensed : 332
ATM Closed
"""


print("=== ATM Cash Dispenser ===\n")

notes = [100, 50, 20, 10, 5, 1]
customers = 0
total_amount = 0

while True:
    name = input("What's your name?")
    amount = int(input("How much money do you want to dispense?"))
    print(f"Dispensing {amount} units:")

    remaining = amount
    index = 0
    length = len(notes)

    while index <= 5:
        count = remaining // notes[index]
        remaining = remaining % notes[index]
        print(count, notes[index])
        index +=1

    customers += 1
    total_amount += amount
    print(f"total amount: {total_amount}")
    print(f"customers: {customers}")
    choice = input("Serve another costomer? yes/no")
    if choice == "no" :
        break

print("ATM Closed")