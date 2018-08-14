# age = 19
# number = 12


def is_adult(age):
    return age >= 18


print("Got {}, expected True".format(is_adult(18)))
print("Got {}, expected False".format(is_adult(17)))
print()


def is_even_number(number):
    return number % 2 == 0


print("Is {} even? {}".format(12, is_even_number(12)))
print()


def square_number(integer):
    return integer ** 2


print("The number {} squared is {}".format(12, square_number(12)))
