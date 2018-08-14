# Task 1
OUT_FILE = open("Output.txt", "w")
enter_name = str(input("Enter your name: "))
print(enter_name, file=OUT_FILE)
OUT_FILE.close()

# Task 2
IN_FILE = open("Output.txt", "r")
name_is = IN_FILE.read()
print("Your name is {}".format(name_is))
IN_FILE.close()

# Task 3 / 4
IN_FILE = open("numbers.txt", "r")
total = 0
for line in IN_FILE:
    total += int(line)
IN_FILE.close()
print(total)
