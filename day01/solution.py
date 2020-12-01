import itertools
import math


class Logic:
    report = list()

    def __init__(self, filename):
        self.report = [int(i) for i in open(filename).read().splitlines()]

    def program(self, number):
        all_combinations = list(itertools.combinations(self.report, number))
        found = next(combination for combination in all_combinations if sum(combination) == 2020)
        solution = math.prod(found)
        print("Found combination " + str(found) + " total is " + str(solution))
        return solution
