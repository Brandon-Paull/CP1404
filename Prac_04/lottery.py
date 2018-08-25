import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick Picks - generate random numbers """
    rounds = int(input("How many quick picks? "))
    while rounds <= 0:
        print("Rounds must be greater than 0")
        rounds = int(input("How many quick picks? "))

    for i in range(rounds):
        picks = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in picks:
                number = random.randint(MINIMUM, MAXIMUM)
            picks.append(number)
        picks.sort()
        print(" ".join("{:2}".format(number) for number in picks))


main()
