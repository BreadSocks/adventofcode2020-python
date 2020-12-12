lines = open("input.txt").read().splitlines()
actions = [[x[:1], int(x[1:])] for x in lines]
x = 0
y = 0
wx = 10
wy = 1

for direction in actions:
    command = direction[0]
    distance = direction[1]
    if command == "N":
        wy += distance
    elif command == "S":
        wy -= distance
    elif command == "E":
        wx += distance
    elif command == "W":
        wx -= distance
    elif command == "R":
        for _ in range(0, distance // 90):
            wx, wy = wy, -wx
    elif command == "L":
        for _ in range(0, distance // 90):
            wx, wy = -wy, wx
    elif command == "F":
        x += wx * distance
        y += wy * distance
print([x, y, wx, wy])
print(sum([abs(x), abs(y)]))
