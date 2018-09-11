from Prac_06.Guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ").strip()

    while name != "":
        year = int(input("Year: "))
        cost = int(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added!")
        name = input("Name: ").strip()

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")

    if len(guitars) != 0:
        for i, guitar in enumerate(guitars):
            vintage_string = "(vintage)" if guitar.is_vintage() else ""
            print("Guitar {}: {:15} ({:4}), worth ${:12,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                       vintage_string))
    else:
        print("You don't own any guitars :(")


main()
