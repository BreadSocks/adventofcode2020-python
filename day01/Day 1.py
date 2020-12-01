import itertools
import math

file = "input.txt"
expense_report = [int(i) for i in open(file).read().splitlines()]


def program(number):
    all_combinations = list(itertools.combinations(expense_report, number))
    found = next(combination for combination in all_combinations if sum(combination) == 2020)
    print("Found combination " + str(found) + " total is " + str(math.prod(found)))


program(2)
program(3)
