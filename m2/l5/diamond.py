"""
OUTPUT:

    *
   ***
  *****
 *******
*********




    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""



"""
    *  1
   ***  3
  *****  5
 *******  7
*********  9
"""


rows = 4
rows = int(input("enter the number of rows: "))
for row in range(rows):
    for col in range(rows - row):
        print(" ", end="") 

    for col in range(2*row + 1):
        print("*", end="")
    print()

for row in range(rows - 1, -1, -1):
    for col in range(rows - row):
        print(" ", end="") 

    for col in range(2*row - 1):
        print("", end="")
    print()