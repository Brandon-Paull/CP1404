
while True:
    try:
        age = int(input("Age: "))
        break
    except ValueError:
            print("Error")

if age % 2 == 0:
    print("Even")
else:
    print("Odd")

