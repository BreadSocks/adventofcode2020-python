import math


class Solution:
    grid = list()
    height = 0
    width = 0

    def __init__(self, filename):
        self.grid = open(filename).read().split()
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def part_one(self):
        slopes = [(3, 1)]
        return self.weeee(slopes)[0]

    def part_two(self):
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        return math.prod(self.weeee(slopes))

    def weeee(self, slopes):
        results = []
        for slope in slopes:
            line_number = slope[1]
            character_position = slope[0]
            landed = []
            while line_number < self.height:
                line = self.grid[line_number]
                character = line[character_position % len(line)]
                landed.append(character)
                line_number += slope[1]
                character_position += slope[0]
            found_trees = landed.count("#")
            results.append(found_trees)
        return results
