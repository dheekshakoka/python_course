num1 = int(input("Pick a number"))
num2 = int(input("Pick a higher number"))

l = range(num1, num2 + 1)

s = 0
for i in l:
    print(i)
    s += i

print("The sum is", s)
