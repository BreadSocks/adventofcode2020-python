instructions = open("input.txt").read().splitlines()

programs_to_try = [instructions]
indexes_already_replaced = []

for index, instruction in enumerate(instructions):
    command = instruction.split()
    if command[0] == "jmp" or command[0] == "nop":
        if index in indexes_already_replaced:
            continue
        elif command[0] == "jmp":
            new_command = "nop"
        else:
            new_command = "jmp"
        new_line = new_command + " " + command[1]
        program = instructions.copy()
        program[index] = new_line
        programs_to_try.append(program)
        indexes_already_replaced.append(index)

for program_to_try in programs_to_try:
    index = 0
    accumulator = 0
    visited_indexes = []
    while True:
        if index in visited_indexes:
            # go to next attempt
            # print(accumulator)
            break
        if index == len(program_to_try):
            # found
            print(accumulator)
            break
        visited_indexes.append(index)
        instruction = program_to_try[index]
        command = instruction.split()
        if command[0] == "acc":
            accumulator += int(command[1])
            index += 1
        elif command[0] == "jmp":
            index += int(command[1])
        elif command[0] == "nop":
            index += 1
