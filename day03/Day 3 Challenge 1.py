grid = open("input.txt").read().split()
width = len(grid[0])  # length of the line
height = len(grid)

line_number = 1
character_position = 3
landed = []
while line_number < height:
    line = grid[line_number]
    character = line[character_position % len(line)]
    landed.append(character)
    line_number += 1
    character_position += 3

print(landed.count("#"))
