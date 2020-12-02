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
    password_parts = [int(part) for part in parts[0].split("-")]
    password_position_one = password_parts[0]
    password_position_two = password_parts[1]
    letter = parts[1]
    if password[password_position_one - 1] == letter and password[password_position_two - 1] == letter:
        continue
    elif password[password_position_one - 1] == letter or password[password_position_two - 1] == letter:
        valid += 1
    else:
        invalid += 1

print("Found invalid: " + str(invalid) + " and valid: " + str(valid))
