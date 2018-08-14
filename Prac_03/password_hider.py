MIN_LENGTH = 5


def main():
    password = get_password()
    print_output(password)


def get_password():
    print("Password must be at least {} characters long".format(MIN_LENGTH))
    password = input("Password: ")
    while len(password) < MIN_LENGTH:
        password = input("Password: ")
    return password


def print_output(password):
    for char in range(len(password)):
        print("*", end="")


main()
