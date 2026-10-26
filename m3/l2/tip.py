def tip(amount, percent):
    tip = (percent / 100) * amount
    return tip

amount = int(input("Enter the amount: "))
percent = int(input("Enter the percentage: "))

tip = tip(amount, percent)
print(tip)
