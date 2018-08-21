numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

total = 0
for number in numbers:
    total += number

print("The first number is ", numbers[0])
print("The last number is ", numbers[-1])
print("The smallest number is ", min(numbers))
print("The largest number is ", max(numbers))
print("The average of the numbers is ", total/len(numbers))

