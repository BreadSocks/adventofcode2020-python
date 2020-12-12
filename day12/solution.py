class Solution:
    actions = []
    x_multipliers = {"N": 0, "S": 0, "E": 1, "W": -1}
    y_multipliers = {"N": 1, "S": -1, "E": 0, "W": 0}

    def __init__(self, filename):
        self.actions = [[x[:1], int(x[1:])] for x in open(filename).read().splitlines()]

    def part_one(self):
        facing = 90
        x = 0
        y = 0

        angle_x_multipliers = {0: 0, 90: 1, 180: 0, 270: -1}
        angle_y_multipliers = {0: 1, 90: 0, 180: -1, 270: 0}
        direction_multipliers = {"L": -1, "R": 1}

        for direction in self.actions:
            command = direction[0]
            distance = direction[1]
            if command in self.x_multipliers.keys():
                x += (self.x_multipliers[command] * distance)
                y += (self.y_multipliers[command] * distance)
            elif command in direction_multipliers.keys():
                facing += (direction_multipliers[command] * distance)
            elif command == "F":
                x += (angle_x_multipliers[facing % 360] * distance)
                y += (angle_y_multipliers[facing % 360] * distance)
        return abs(x) + abs(y)

    def part_two(self):
        x = 0
        y = 0
        wx = 10
        wy = 1

        for direction in self.actions:
            command = direction[0]
            distance = direction[1]
            if command in self.x_multipliers.keys():
                wx += (self.x_multipliers[command] * distance)
                wy += (self.y_multipliers[command] * distance)
            elif command == "R":
                for _ in range(0, distance // 90):
                    wx, wy = wy, -wx
            elif command == "L":
                for _ in range(0, distance // 90):
                    wx, wy = -wy, wx
            elif command == "F":
                x += wx * distance
                y += wy * distance
        return abs(x) + abs(y)
