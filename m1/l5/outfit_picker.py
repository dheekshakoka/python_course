"""
Activity: Weather Outfit Picker

Instructions:
1. Ask the user to enter today's temperature.
2. If the temperature is below 20°C, suggest wearing a jacket.
3. Otherwise, suggest wearing a t-shirt.
4. Ask if it is raining.
5. If it is raining, remind the user to carry an umbrella.
6. Ask if there are puddles on the ground.
7. If there are puddles, suggest wearing boots.
8. Otherwise, suggest wearing sneakers.
9. Display a summary of the outfit choices.
"""

# Ask for today's temperature
temperature = int(input("What's the temperature?"))
outfit = "T-shirt"
# Check if it is cold and decide the outfit 
if temperature < 20:
    print("Wear a jacket.")
    outfit = "Jacket"
else:
    print("Wear a T-shirt")

# Check if it is raining and decide on the umbrella
raining = input("Is it raining?")
umbrella = "No umbrella"
if raining == "yes":
    print("Carry an umbrella.")
    umbrella = "Umbrella"


# Check for puddles and decide the shoes
puddles = input("Are there any puddles?")
shoes = "Any shoes"
if puddles == "yes":
    print("Wear boots.")
    shoes = "boots"
else:
    print("Wear any other shoes.")

# Display the final summary
print()
print("This is your final outfit for today:")
print()
print("----------------")
print(outfit)
print(umbrella)
print(shoes)
print("----------------")
print()