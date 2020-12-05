from day05.boardingpass import BoardingPass


class Solution:
    boarding_passes = []

    def __init__(self, filename):
        self.boarding_passes = [BoardingPass(x) for x in open(filename).read().splitlines()]

    def part_one(self):
        return max(x.seatId for x in self.boarding_passes)

    def part_two(self):
        seat_ids = list(map(lambda x: x.seatId, self.boarding_passes))
        missing_ids = [x for x in list(range(0, 1024)) if x not in seat_ids]
        found = [missing_id for missing_id in missing_ids if (missing_id + 1) in seat_ids and (missing_id - 1) in seat_ids]
        return found[0]
