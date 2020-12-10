numbers = [int(i) for i in open("input.txt").read().splitlines()]
numbers.append(0)  # our starting point
numbers = sorted(numbers)
numbers.append(numbers[-1] + 3)  # our end point

diff_map = {}
for number in numbers:
    further = [number + x for x in range(1, 4) if number + x in numbers]  # 1-3
    diff_map[number] = further

done = {0: numbers[1]}  # initialise with 0 and a startin gpoint
for key, values in diff_map.items():
    for value in values:
        if value in done.keys():
            done[value] += done[key]  # keep count that we've visited
        else:
            done[value] = done[key]
print(diff_map)
print(done)
print(done[numbers[-1]])
