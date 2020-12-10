numbers = sorted([int(i) for i in open("input.txt").read().splitlines()])
diffs = []
for index, number in enumerate(numbers):
    if index == 0:
        diffs.append(number)
    else:
        diffs.append(number - numbers[index - 1])
        print(numbers)
diffs.append(3)
print("1 jolt differences: " + str(diffs.count(1)) + " and 3 jolt differences: " + str(diffs.count(3)))
