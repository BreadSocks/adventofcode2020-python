import collections
file = "input.txt"

lines = [line for line in open(file).read().splitlines()]
password_db = list()
for line in open(file).read().splitlines():
    parts = line.split(": ")
    password_db.append(dict({parts[0]: parts[1]}))

invalid = 0
valid = 0
for password_dict in password_db:
    rule = list(password_dict.keys())[0]
    password = password_dict[rule]
    parts = rule.split(" ")
    password_min_max = [int(part) for part in parts[0].split("-")]
    password_range = range(password_min_max[0], password_min_max[1])
    occurrences = password.count(parts[1])
    sum_example = sum(parts[1] == letter for letter in password)
    if password_min_max[0] <= occurrences <= password_min_max[1]:
        valid += 1
    else:
        invalid += 1

print("Found invalid: " + str(invalid) + " and valid: " + str(valid))
