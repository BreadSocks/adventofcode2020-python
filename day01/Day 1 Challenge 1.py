import itertools
file = "input.txt"

expense_report = [int(i) for i in open(file).read().splitlines()]
all_combinations = list(itertools.combinations(expense_report, 2))
for combination in all_combinations:
    if sum(combination) == 2020:
        print("Found numbers " + str(combination) + " that make 2020. Multiplied together equals " + str(combination[0] * combination[1]))
        break
