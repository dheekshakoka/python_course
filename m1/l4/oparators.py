"""
Harvest farm programming in python.
Author: Dheeksha Koka
Date: 10-08-2026
"""
# --- Assignment Operator (=) ---
# Store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average harvest
total = field1 + field2 + field3 + field4 + field5
average = total/5
print("The total is:", total)
print(f"The average is: {average}")


# Price per kg is 15 rupees — calculate total earnings
price_per_kg = 15

earnings = price_per_kg*total
print("The total earnings are:", earnings)

# --- Floor Division (//) and Modulus (%) ---
# Pack the harvest into bags of 25 kg each

amount_of_bags = total//25 
remaining = total%25
print("The amount of full bags are:", amount_of_bags)
print("The remaining amount will be:", remaining)


# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Is last years harvest equal to this year?", last_year == total)
print("Is last years harvest less than or equal to this year?", last_year <= total)
print("Is last years harvest greater than or equal to this year?", last_year >= total)


# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total
total += 30 #total = total + 30 
print(total)
