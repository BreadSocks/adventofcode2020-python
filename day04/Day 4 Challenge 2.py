import re

from day04.passport import Passport

file = open("input.txt").read().split("\n\n")
entries = []
for passport in file:
    data = dict(x.split(":") for x in re.split("[ \n]+", passport))
    passport = Passport(data)
    entries.append(passport)

print(sum(x.valid for x in entries))

