import bisect

passes = open("input.txt").read().splitlines()
seatIds = []

for boarding_pass in passes:
    lower = 0
    upper = 127
    for character in boarding_pass[0:7]:
        if character == "F":
            upper = lower + (upper - lower) // 2  # floor division
        if character == "B":
            lower = lower + -(-(upper - lower) // 2)
            # lower = -(-upper // 2)  # hacky ceiling division

    if lower == upper:
        print("found row: " + str(lower))
    else:
        print("didn't find row - lower : " + str(lower) + " upper : " + str(upper))
        exit(1)

    row = lower
    lower = 0
    upper = 7
    for character in boarding_pass[7:10]:
        if character == "L":
            upper = lower + (upper - lower) // 2  # floor division
        if character == "R":
            lower = lower + -(-(upper - lower) // 2)
            # lower = -(-upper // 2)  # hacky ceiling division

    if lower == upper:
        print("found column: " + str(lower))
    else:
        print("didn't find column - lower : " + str(lower) + " upper : " + str(upper))
        exit(1)

    column = lower

    seatId = (row * 8) + column
    seatIds.append(seatId)

missing = [x for x in list(range(0, 1024)) if x not in seatIds]
print(missing)
for missed in missing:
    if (missed + 1) in seatIds and (missed - 1) in seatIds:
        print("Found:" + str(missed))
