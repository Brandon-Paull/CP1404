# Task 1
out_file = open("Output.txt", "w")
enter_name = str(input("Enter your name: "))
print(enter_name, file=out_file)
out_file.close()

# Task 2
in_file = open("Output.txt", "r")
name_is = in_file.read()
print("Your name is {}".format(name_is))
in_file.close()

# Task 3 / 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    total += int(line)
print(total)

