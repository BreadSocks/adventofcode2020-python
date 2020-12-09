import itertools

numbers = [int(i) for i in open("input.txt").read().splitlines()]
preamble = 25


def number_to_find():
    for index in range(preamble, len(numbers)):
        number = numbers[index]
        combinations = numbers[index - preamble:index]
        attempts = list(itertools.combinations(combinations, 2))
        found = False
        for attempt in attempts:
            if sum(attempt) == number:
                found = True

        if not found:
            return number


find = number_to_find()
for index, number in enumerate(numbers):
    nums = [number]
    index_offset = 1
    while sum(nums) < find:
        new_num = numbers[index + index_offset]
        nums.append(new_num)
        index_offset += 1
    if sum(nums) == find:
        # print(nums)
        sorted_nums = sorted(nums)
        print(sorted_nums[0] + sorted_nums[-1])
        break
