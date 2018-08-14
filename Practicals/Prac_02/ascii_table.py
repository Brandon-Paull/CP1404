"""
ord() --> Character to ordinal
chr() --> Ordinal to character
"""

LOWER_BOUND = 33
UPPER_BOUND = 127

input_character = input("Enter a character: ")

while input_character.isnumeric():
    input_character = input("Please Enter a valid character: ")

ascii_output = ord(input_character)
print("The ASCII code for {} is {}".format(input_character, ascii_output))

input_number = int(input("Enter a number between {} and {}: ".format(LOWER_BOUND, UPPER_BOUND)))
while input_number < LOWER_BOUND or input_number > UPPER_BOUND:
    input_number = input("Enter a valid integer: ")
character_output = chr(input_number)
print("The character for {} is {}".format(input_number, character_output))

view_table = input("View ASCII TABLE? (Y/N): ").upper()
if view_table == "Y":
    number_columns = int(input("How many columns?: "))
    number_columns += 1

    # TODO create multiple columns
     for i in range(number_columns):

        # for j in range(LOWER_BOUND, (UPPER_BOUND // number_columns)):
        #     print("{:>3} ... {}\t\t".format(j, chr(j)))
