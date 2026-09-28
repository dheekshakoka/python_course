"""
OUTPUT:

Please Enter the total Number of Rows  : 4
1  
2  3  
4  5  6  
7  8  9  10 
"""
rows = int(input("enter the number of rows: "))

num = 1
for row in range(rows + 1):
    for col in range(row):
        print(num, end=" ")
        num +=1
    print()
