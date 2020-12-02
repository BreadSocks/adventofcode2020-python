class PassEntry:
    password = ""
    character = ""
    minimum_occurrences = 0
    maximum_occurrences = 0
    first_position = 0
    second_position = 0

    def __init__(self, line):
        parts = line.split(": ")
        rule = parts[0]
        rule_parts = rule.split(" ")
        number_parts = rule_parts[0]
        numbers = number_parts.split("-")

        self.password = parts[1]
        self.character = rule_parts[1]
        self.minimum_occurrences = int(numbers[0])
        self.maximum_occurrences = int(numbers[1])
        self.first_position = self.minimum_occurrences - 1
        self.second_position = self.maximum_occurrences - 1
