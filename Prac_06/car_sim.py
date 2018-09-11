from Prac_06.car import Car


MENU = """
Menu:
d) drive
r) refuel
q) quit
"""


def main():
    print("Let's drive!")
    my_car = Car(input("Enter your car name: "), 100)
    print("{}, fuel={}, odo={}".format(my_car.name, my_car.fuel, my_car.odometer))
    print(MENU)

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "D":
            drive_car(my_car)
        elif choice == "R":
            refuel_car(my_car)
        else:
            print("Invalid menu choice")
        print()
        print(my_car)
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye {}'s owner".format(my_car.name))


def drive_car(my_car):
    distance = int(input("How many km do you wish to drive? "))
    while distance <= 0:
        print("Distance must be > 0")
        distance = int(input("How many km do you wish to drive? "))

    if my_car.fuel <= distance:
        possible_distance = my_car.fuel
        print("The car drove, {}km and ran out of fuel.".format(possible_distance))
    else:
        possible_distance = distance
        print("The car drove, {}km.".format(possible_distance))
    my_car.drive(possible_distance)


def refuel_car(my_car):
    fuel_to_add = int(input(" How many units of fuel do you want to add to the car? "))
    while fuel_to_add <= 0:
        print(" Fuel amount must be >= 0")
        fuel_to_add = int(input(" How many units of fuel do you want to add to the car? "))
    print("Added {} units of fuel.".format(fuel_to_add))
    my_car.add_fuel(fuel_to_add)


main()
