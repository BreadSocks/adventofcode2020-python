import itertools

groups = open("input.txt").read().split("\n\n")
count = 0
for group_answers in groups:
    count += len(set(list(itertools.chain.from_iterable(group_answers.split("\n")))))

print(count)
