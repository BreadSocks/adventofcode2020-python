import math

grid = open("input.txt").read().split()
width = len(grid[0])
height = len(grid)

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
for slope in slopes:
    line_number = slope[1]
    character_position = slope[0]
    landed = []
    while line_number < height:
        line = grid[line_number]
        character = line[character_position % len(line)]
        landed.append(character)
        line_number += slope[1]
        character_position += slope[0]
    found_trees = landed.count("#")
    results.append(found_trees)

print(results)
print(math.prod(results))
