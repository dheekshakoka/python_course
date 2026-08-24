a = int(input("Give a number")) 
b = int(input("Give a number")) 
c = int(input("Give a number")) 

average = (a + b + c)/3
print(average)

greatest = 0

if a > b and a > c:
    greatest = a
    print("a is the greatest")
elif b > a and b > c:
    greatest = b
    print("b is the greatest")
elif c > a and c > b:
    greatest = c
    print("c is the greatest")

print(greatest)

