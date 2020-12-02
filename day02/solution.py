from day02.PassEntry import PassEntry


class Solution:
    password_database = list()

    def __init__(self, filename):
        self.password_database = [PassEntry(line) for line in open(filename).read().splitlines()]

    def part_one(self):
        return sum(entry.password.count(entry.character) in range(entry.minimum_occurrences, entry.maximum_occurrences + 1) for entry in self.password_database)

    def part_two(self):
        return sum((entry.password[entry.first_position] == entry.character) != (entry.password[entry.second_position] == entry.character) for entry in self.password_database)
