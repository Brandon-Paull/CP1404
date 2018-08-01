
number_of_items = int(input("Number of items: "))
total = 0
while number_of_items <= 0:
    print("Invalid number of items")
    print("\n")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9
print("Total price for ", number_of_items, " item(s) is $", total, sep='')

