from Prac_06.person import Person

MENU = """
A - Add person
L - List people
Q - Quit
"""


def main():
    print(MENU)
    person1 = Person("Brandon", "Paull", 19)
    person2 = Person("Thanos", "The Mad Titan", 2000)
    people = [person1, person2]

    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            age = int(input("Age: "))
            people.append(Person(first_name, last_name, age))
        elif choice == "L":
            print(people)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Byeeee")


if __name__ == '__main__':
    main()
