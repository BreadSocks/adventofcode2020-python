import itertools
file = "input.txt"

expense_report = [int(i) for i in open(file).read().splitlines()]
all_combinations = list(itertools.combinations(expense_report, 3))
for combination in all_combinations:
    if sum(combination) == 2020:
        print("Found numbers "
              + str(combination[0]) + " and " + str(combination[1]) + " and " + str(combination[2]) +
              " that make 2020. Multiplied together equals " + str(combination[0] * combination[1] * combination[2]))
        break
