"""
# 1. Bike 
#     1. Mountain Bike
#     2. Sports Bike
# 2. Car
#     1. Sedan
#     2. SUV
"""

"""
OUTPUT:
Pick your vehicle. 1 - Bike, 2 - Car
Enter your choice: 1
You picked Bike

Pick your bike type. 1 - Sports Bike, 2 - Mountain Bike
Enter your choice: 2
You picked Mountain Bike

Thank you
"""

vehicle_type = int(input("Pick your vehicle type: 1. car 2. Bike"))
if vehicle_type == 1:
    print("You picked car.")
    car_type = int(input("Pick your car type: 1. Sudan 2. SUV"))
    if car_type == 1:
        print("You picked Sudan.")
    elif car_type == 2:
        print ("You picked SUV.")
    else:
        print("Invalid choise.")

if vehicle_type == 2:
    print("You picked bike.")
    bike_type = int(input("Pick your bike type: 1. mountain 2. sports"))
    if bike_type == 1:
        print("You picked mountain.")
    elif bike_type == 2:
        print ("You picked sports.")
    else:
        print("Invalid choise.")
