import random

print("Welcome to the gopher population simulator!")


def main():
    population = 1000
    year = 1
    print("Starting population: {:.0f}".format(population))
    print("Year {}".format(year))
    print("\n")

    while year < 10:
        population_increase = calculate_population_increase(population)
        population_decrease = calculate_population_decrease(population)
        population = population + population_increase - population_decrease
        print_change(population, population_increase, population_decrease)
        year += 1
        print("Year {}".format(year))
        print("\n")


def calculate_population_increase(population):
    population_increase = random.uniform(0.1, 0.2) * population
    return population_increase


def calculate_population_decrease(population):
    population_decrease = random.uniform(0.05, 0.25) * population
    return population_decrease


def print_change(population, population_increase, population_decrease):
    print("{:.0f} gophers were born. {:.0f} died.".format(population_increase, population_decrease))
    print("Population: {:.0f}".format(population))
    return population


main()
