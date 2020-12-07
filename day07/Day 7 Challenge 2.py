import re

lines = open("input.txt").read().splitlines()
mapping = dict()
for line in lines:
    major_split = line.split(" bags contain ")
    key = major_split[0]
    if major_split[1] == "no other bags.":
        mapping[key] = None
    else:
        colours = major_split[1].strip(".").split(", ")
        for colour in colours:
            value = re.sub(r"[0-9]\s|\b\sbag\w|\b\sbag+", "", colour)
            number = int(colour.split(value)[0])
            if mapping.get(key) is None:
                mapping[key] = {value: number}
            else:
                mapping[key][value] = number


def loop(colours_quantities):
    inner_count = 0
    for col, quantity in colours_quantities.items():
        if mapping.get(col) is None:
            inner_count += quantity
        else:
            inner_count += quantity + (quantity * loop(mapping[col]))
    return inner_count


print(loop(mapping["shiny gold"]))
