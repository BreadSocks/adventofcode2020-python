import itertools


class Solution:
    numbers = []

    def __init__(self, filename):
        self.numbers = [int(i) for i in open(filename).read().splitlines()]

    def part_one(self, preamble):
        for index in range(preamble, len(self.numbers)):
            number = self.numbers[index]
            combinations = self.numbers[index - preamble:index]
            attempts = list(itertools.combinations(combinations, 2))
            found = False
            for attempt in attempts:
                if sum(attempt) == number:
                    found = True

            if not found:
                return number

    def program(self, preamble):
        for index in range(preamble, len(self.numbers)):
            number = self.numbers[index]
            combinations = self.numbers[index - preamble:index]
            attempts = list(itertools.combinations(combinations, 2))
            found = any(sum(attempt) == number for attempt in attempts)
            found = False
            for attempt in attempts:
                if sum(attempt) == number:
                    found = True

            if not found:
                return number
