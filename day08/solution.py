class Solution:
    instructions = []

    def __init__(self, filename):
        self.instructions = open(filename).read().splitlines()

    def part_one(self):
        return self.run_program(self.instructions, True)

    def part_two(self):
        programs_to_try = [self.instructions]
        indexes_already_replaced = []

        for index, instruction in enumerate(self.instructions):
            command = instruction.split()
            if command[0] == "jmp" or command[0] == "nop":
                if index in indexes_already_replaced:
                    continue
                elif command[0] == "jmp":
                    new_command = "nop"
                else:
                    new_command = "jmp"
                new_line = new_command + " " + command[1]
                program = self.instructions.copy()
                program[index] = new_line
                programs_to_try.append(program)
                indexes_already_replaced.append(index)

        for program_to_try in programs_to_try:
            result = self.run_program(program_to_try, False)
            if result is not None:
                return result

    def run_program(self, program, is_part_one):
        index = 0
        accumulator = 0
        visited_indexes = []
        while True:
            if index in visited_indexes:
                if is_part_one:
                    return accumulator
                else:
                    return None
            if index == len(program):
                # found
                if is_part_one:
                    return None
                else:
                    return accumulator
            visited_indexes.append(index)
            instruction = program[index]
            command = instruction.split()
            if command[0] == "acc":
                accumulator += int(command[1])
                index += 1
            elif command[0] == "jmp":
                index += int(command[1])
            elif command[0] == "nop":
                index += 1
