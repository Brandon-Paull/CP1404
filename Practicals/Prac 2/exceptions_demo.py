"""
1. If integers aren't entered, eg. floating numbers, letters etc.
2. When the denominator is a 0
3. Include while loop and don't let a 0 pass into calculation
"""
valid_input = False
while not valid_input:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator must be greater than 0")
        else:
            fraction = numerator / denominator
            print(fraction)
            valid_input = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
print("Finished.")
