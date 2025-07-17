import re


def parse_int(instruction: str) -> tuple[int, int]:
    numbers = re.findall(r'\d+', instruction)

    return (int(numbers[0]), int(numbers[1]))

def parse_instruction(line: str):
    pattern = r'mul\((\d+),(\d+)\)|do\(\)|don\'t\(\)'
    results = []
    enabled = True
    enable_instruction = None

    for match in re.finditer(pattern, line):
        if enabled and match.group(1):
            results.append(match.group(1))

        if match.group(2):
            enable_instruction = str(match.group(2))
        elif match.group(3):
            enable_instruction = str(match.group(3))
        else:
            enable_instruction = "do()"

        enabled = toggle_add_instruction(enable_instruction)

    return results


def toggle_add_instruction(instruction: str | None) -> bool:
    if instruction == "don't()":
        return False
    return True


if __name__ == "__main__":
    sum_part_1 = 0
    with open("example.txt", "r") as f:
        for line in f:
            mul_instructions = re.findall(r"mul\(\d+,\s*\d+\)", line)
            enabled_mul_instructions = parse_instruction(line)
            print(enabled_mul_instructions)

            for match in mul_instructions:
                num1_part_1, num2_part_1 = parse_int(match)
                sum_part_1 += num1_part_1 * num2_part_1

    print(sum_part_1)
