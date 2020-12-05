class BoardingPass:
    row = 0
    column = 0
    seatId = 0

    def __init__(self, boarding_pass):
        self.row = self.search(0, 127, boarding_pass[0:7])
        self.column = self.search(0, 7, boarding_pass[7:10])
        self.seatId = (self.row * 8) + self.column

    def search(self, lower, upper, boarding_pass):
        for character in boarding_pass:
            if character == "F" or character == "L":
                upper = lower + (upper - lower) // 2  # floor division
            if character == "B" or character == "R":
                lower = lower + -(-(upper - lower) // 2)  # hacky ceiling division
        return upper
