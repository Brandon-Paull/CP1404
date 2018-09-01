
def main():
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
    print(list_to_dictionary(names, dates_of_birth))


def list_to_dictionary(names, dates_of_birth):
    name_to_age = dict(zip(names, dates_of_birth))
    return name_to_age


main()
