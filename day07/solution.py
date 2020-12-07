import re


class Solution:
    mapping = dict()

    def __init__(self, filename):
        lines = open(filename).read().splitlines()
        for line in lines:
            major_split = line.split(" bags contain ")
            key = major_split[0]
            if major_split[1] == "no other bags.":
                self.mapping[key] = None
            else:
                colours = major_split[1].strip(".").split(", ")
                for colour in colours:
                    value = re.sub(r"[0-9]\s|\b\sbag\w|\b\sbag+", "", colour)
                    number = int(colour.split(value)[0])
                    if self.mapping.get(key) is None:
                        self.mapping[key] = {value: number}
                    else:
                        self.mapping[key][value] = number

    def part_one(self):
        found = set()
        count = 0
        for colour, colours in self.mapping.items():
            if colours is not None and "shiny gold" in colours:
                found.add(colour)

        while len(found) != count:
            count = len(found)
            for colour, colours, in self.mapping.items():
                for found_colour in found.copy():
                    if colours is not None and found_colour in colours:
                        found.add(colour)
        return len(found)

    def part_two(self):
        return self.count_loop(self.mapping["shiny gold"])

    def count_loop(self, colours_quantities):
        inner_count = 0
        for col, quantity in colours_quantities.items():
            if self.mapping.get(col) is None:
                inner_count += quantity
            else:
                inner_count += quantity + (quantity * self.count_loop(self.mapping[col]))
        return inner_count
