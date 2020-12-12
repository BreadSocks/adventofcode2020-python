lines = open("input.txt").read().splitlines()
actions = [[x[:1], int(x[1:])] for x in lines]
facing = 90
x = 0
y = 0

for direction in actions:
    command = direction[0]
    distance = direction[1]
    if command == "N":
        y += distance
    elif command == "S":
        y -= distance
    elif command == "E":
        x += distance
    elif command == "W":
        x -= distance
    elif command == "R":
        facing += distance
    elif command == "L":
        facing -= distance
    elif command == "F":
        if facing % 360 == 90:
            x += distance
        elif facing % 360 == 180:
            y -= distance
        elif facing % 360 == 270:
            x -= distance
        elif facing % 360 == 0:
            y += distance
print(sum([abs(x), abs(y)]))
