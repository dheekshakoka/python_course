"""
===== SNACK VENDING MACHINE =====
Snack Price: 25
Accepted Coins: [1, 5, 10, 25]
Insert a coin: 5
Total Inserted: 5
Insert a coin: 6
Invalid coin! Try again.
Insert a coin: 10
Total Inserted: 15
Insert a coin: 5
Total Inserted: 20
Insert a coin: 10
Total Inserted: 30

Dispensing your snack...
Change Returned: 5

===== PURCHASE SUMMARY =====
Snack Price: 25
Total Paid: 30
Change Given: 5
Thank you for your purchase!
"""

print("===== SNACK VENDING MACHINE =====")

snackprice = 25
accepted_coins = [1, 5, 10, 25]
print("The sack price is", snackprice)
total = 0
while True:
    coin = int(input("insert your coins: "))
    if coin in accepted_coins:
        total += coin
    else:
        print("invalid coin")
    if total >= snackprice:
        break
change = total - snackprice
print("===== PURCHASE SUMMARY =====" )
print(f"Snack price: 25, total paid: {total}, Change: {change}")

