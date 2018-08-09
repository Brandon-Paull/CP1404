SECRET_NUMBER = 7

guess = int(input("Guess: "))
while guess != SECRET_NUMBER:
    print("Incorrect")
    guess = int(input("Guess: "))
print("Correct")
