YEAR = 2018
names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

people = {}
for i in range(0, 5):
    name = input("Name: ")
    date_of_birth = input("dd/mm/yyyy: ")
    people[name] = 2019 - int(date_of_birth.split("/")[2])


print(people)
