import itertools

numbers = [int(i) for i in open("input.txt").read().splitlines()]
preamble = 25

for index in range(preamble, len(numbers)):
    number = numbers[index]
    range = numbers[index - preamble:index]
    attempts = list(itertools.combinations(range, 2))
    found = False
    for attempt in attempts:
        if sum(attempt) == number:
            found = True

    if not found:
        print(number)
