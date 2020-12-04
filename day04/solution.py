import re

from day04.passport import Passport


class Solution:
    entries = list()
    passports = list()

    def __init__(self, filename):
        self.entries = [dict(x.split(":") for x in re.split("[ \n]+", passport)) for passport in open(filename).read().split("\n\n")]
        self.passports = [Passport(passport) for passport in self.entries]

    def part_one(self):
        return sum(x.hasRequiredFields for x in self.passports)

    def part_two(self):
        return sum(x.valid for x in self.passports)
