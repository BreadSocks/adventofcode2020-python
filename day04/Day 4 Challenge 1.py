import re

file = open("input.txt").read().split("\n\n")
entries = []
for passport in file:
    entries.append(dict(x.split(":") for x in re.split("[ \n]+", passport)))

print(entries)
count = 0
for entry in entries:
    if len(entry.keys()) == 8 or (len(entry.keys()) == 7 and "cid" not in entry.keys()):
        count += 1
print(count)
