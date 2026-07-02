hehe = input("Choose a 1. Vehicle or 2. Bike: ")
if hehe == "1":
    print("You have chosen Vehicle")
    hehe_car = input("What type of vehicle do you want to choose? 1. SUV or 2. Sport Car: ")
    if hehe_car not in ("1", "2"):
        print("Invalid choice for vehicle type")

    if hehe_car == "1":
        print("You have chosen SUV")
    elif hehe_car == "2":
        print("You have chosen Sport Car")
elif hehe == "2":
    
    print("You have chosen Bike")
    hehe_bike = input("What type of bike do you want to choose? 1. Mountain Bike or 2. Road Bike: ")
    if hehe_bike not in ("1", "2"):
        print("Invalid choice for bike type")
    if hehe_bike == "1":
        print("You have chosen Mountain Bike")
    elif hehe_bike == "2":
        print("You have chosen Road Bike")
else:
    print("Invalid choice for bike type")