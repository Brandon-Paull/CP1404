"""Brandon Paull"""

MIN_LENGTH = 5

password = input("Enter password: ")

while len(password) < MIN_LENGTH:
    password = input("Password must be at least {} characters long".format(MIN_LENGTH))

number_characters = len(password)

for i in range(0, number_characters):
    print("*", end="")  # end stops print going to a new line
