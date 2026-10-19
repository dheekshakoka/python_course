
"""
OUTPUT:

Welcome to the Lemonade Stand!
Price per cup is 10

Enter number of cups you want: 4

===== RECEIPT =====
Price Per Cup : 10
Cups sold     : 4
Total Cost    : 40
===================
"""
print("Welcome to the Lemonade Stand!")
price = 10 
print(f"Price per cup is {price}")

def total(num1, num2):
    s = num1*num2
    return s
cups = int(input("Enter number of cups you want: "))
total1 = total(price, cups)
print(f"Your total is: {total1}")