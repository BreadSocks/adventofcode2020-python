import re

lines = open("input.txt").read().splitlines()
mapping = dict()
for line in lines:
    major_split = line.split(" bags contain ")
    key = major_split[0]
    if major_split[1] == "no other bags.":
        mapping[key] = []
    else:
        colours = major_split[1].strip(".").split(", ")
        for colour in colours:
            value = re.sub(r"[0-9]\s|\b\sbag\w|\b\sbag+", "", colour)
            if mapping.get(key) is None:
                mapping[key] = [value]
            else:
                mapping[key].append(value)

found = set()
count = 0
for colour, colours in mapping.items():
    if "shiny gold" in colours:
        found.add(colour)

while len(found) != count:
    count = len(found)
    for colour, colours, in mapping.items():
        for found_colour in found.copy():
            if found_colour in colours:
                found.add(colour)
print(str(len(found)))
