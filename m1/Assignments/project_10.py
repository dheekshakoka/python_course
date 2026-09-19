print("=== Power Calculator ===")

base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))

result = 1

for i in range(1, exponent + 1):
    result = result * base
    print("result =", result)

print("Answer:", base, "to the power", exponent, "=", result)