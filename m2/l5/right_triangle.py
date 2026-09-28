"""
OUTPUT:

enter the number of rows: 4
* 
* * 
* * * 
* * * * 
"""
rows = int(input("enter the number of rows: "))

for row in range(rows + 1):
    for col in range(row):
        print("*", end=" ")
    print()
