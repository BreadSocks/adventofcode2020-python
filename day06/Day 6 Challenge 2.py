import itertools
from collections import Counter

groups = open("input.txt").read().split("\n\n")
count = 0
for group_answers in groups:
    split = group_answers.split("\n")
    number_of_people = len(split)
    letters = set(list(itertools.chain.from_iterable(split)))
    counts = Counter(list(itertools.chain.from_iterable(split)))
    for letter in letters:
        if counts[letter] == number_of_people:
            count += 1

print(count)
