GROUP_AGES = [-1, -3, -1]

total = 0
group_size = len(GROUP_AGES)
count = 0

for i in range(group_size):
    if GROUP_AGES[i] >= 0:
        total += GROUP_AGES[i]
        count += 1
try:
    average = total / count
except ZeroDivisionError:
    print("No valid entries exist")
    average = ""

print(average)
