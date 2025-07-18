import re

def parse_int(instruction: str) -> tuple[int, int]:
    numbers = re.findall(r'\d+', instruction)
    return (int(numbers[0]), int(numbers[1]))

def parse_instruction(line: str):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    results = []
    for match in re.finditer(pattern, line):
        results.append(match.group())
    return results

def remove_instructions(instructions: list[str]):
    new_instructions = []
    enable = True
    for r in range(len(instructions)):
        if instructions[r] == "don't()":
            enable = False
        elif instructions[r] == "do()":
            enable = True
        elif enable and instructions[r].startswith("mul"):  # Changed: use elif instead of if
            new_instructions.append(instructions[r])
    return new_instructions

if __name__ == "__main__":  # Fixed: double underscores
    sum_part_1 = 0
    sum_part_2 = 0

    # Read entire file as one string to maintain state across lines
    with open("input.txt", "r") as f:
        entire_input = f.read()

    # Part 1: Find all mul instructions (no state tracking)
    mul_instructions_part1 = re.findall(r"mul\(\d{1,3},\d{1,3}\)", entire_input)
    for match in mul_instructions_part1:
        num1, num2 = parse_int(match)
        sum_part_1 += num1 * num2

    # Part 2: Process instructions in order with state tracking
    all_instructions = parse_instruction(entire_input)
    enable = True

    for instruction in all_instructions:
        if instruction == "don't()":
            enable = False
        elif instruction == "do()":
            enable = True
        elif enable and instruction.startswith("mul"):
            num1, num2 = parse_int(instruction)
            sum_part_2 += num1 * num2

    print(sum_part_1)
    print(sum_part_2)
