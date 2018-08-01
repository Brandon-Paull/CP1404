for i in range(1, 21, 2):
    print(i, end=' ')
print("\n")

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n")

# c.
number_of_stars = int(input("Number: "))
for i in range(0, number_of_stars):
    print("*", end=" ")
print("\n")

for i in range(number_of_stars):
    print('*' * (i + 1), end=' ')
    print()
