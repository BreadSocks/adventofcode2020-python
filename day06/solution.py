import itertools
from collections import Counter


class Solution:
    groups = []

    def __init__(self, filename):
        self.groups = open(filename).read().split("\n\n")

    def part_one(self):
        return sum(len(set(list(itertools.chain.from_iterable(group_answers.split("\n"))))) for group_answers in self.groups)

    def part_two(self):
        count = 0
        for group_answers in self.groups:
            split = group_answers.split("\n")
            number_of_people = len(split)
            raw_letters = list(itertools.chain.from_iterable(split))
            letters = set(raw_letters)
            counts = Counter(raw_letters)
            count += sum(1 for letter in letters if counts[letter] == number_of_people)
        return count
