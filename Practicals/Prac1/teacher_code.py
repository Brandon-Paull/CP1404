print("Number Sequence generator")

print("(E)ven Numbers")
print("(O)dd Numbers")
print("(S)quare Numbers")
print("(Q)uit")
print()

user_input = input(">> ").upper()


while user_input != "Q":
    # EVEN
    lower_bound = int(input("Select the smaller number: "))
    upper_bound = int(input("Select the larger number: "))

    if user_input == "E":
        if lower_bound % 2 == 0:
            for i in range(lower_bound, upper_bound + 1, 2):
                print(i, end=" ")
        else:
            for i in range(lower_bound + 1, upper_bound + 1, 2):
                print(i, end=" ")
    # ODD
    elif user_input == "O":
        if lower_bound % 2 == 0:
            for i in range(lower_bound + 1, upper_bound + 1, 2):
                print(i, end=" ")
        else:
            for i in range(lower_bound, upper_bound + 1, 2):
                print(i, end=" ")
    elif user_input == "S":
        for i in range(lower_bound, upper_bound + 1):
            print(i*i, end=" ")
    else:
        print("Invalid input")

    print()
    print("Number Sequence generator")
    print("(E)ven Numbers")
    print("(O)dd Numbers")
    print("(S)quare Numbers")
    print("(Q)uit")
    print()
    user_input = input(">> ").upper()
