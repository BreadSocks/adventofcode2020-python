instructions = open("input.txt").read().splitlines()
index = 0
accumulator = 0
visited_indexes = []
while True:
    if index in visited_indexes:
        print(accumulator)
        break
    visited_indexes.append(index)
    instruction = instructions[index]
    command = instruction.split()
    if command[0] == "acc":
        accumulator += int(command[1])
        index += 1
    elif command[0] == "jmp":
        index += int(command[1])
    elif command[0] == "nop":
        index += 1
