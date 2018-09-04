from Prac_06.Guitar import Guitar


name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

guitar = Guitar(name, year, cost)

print("{} get_age() - Expected 96 - Got {}".format(guitar.name, guitar.get_age()))
print("{} is_vintage() - Expected True - Got {}".format(guitar.name, guitar.is_vintage()))
