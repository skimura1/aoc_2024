def check_safety_report(report: list[int]):
    increasing = False
    if report[0] - report[-1] < 0:
        increasing = True

    for i in range(1, len(report)):
        prev = report[i - 1]
        curr = report[i]

        if not is_gradual_change(prev, curr, increasing):
            return False, i

    return True, -1


def is_gradual_change(prev_level: int, curr_level: int, is_increasing: bool) -> bool:
    diff = curr_level - prev_level
    # Check absolute difference constraint: at least 1 and at most 3
    if not (1 <= abs(diff) <= 3):
        return False

    # Check consistency with overall trend (increasing or decreasing)
    if is_increasing:
        return diff > 0
    else:
        return diff < 0


def check_safety_with_dampener(report: list[int], idx: int) -> bool:
    # Try removing the element at idx
    temp_report = report[:idx] + report[idx + 1:]
    safe, _ = check_safety_report(temp_report)  # Fixed the unpacking
    if safe:
        return True
    
    # Also try removing the previous element (idx-1) if it exists
    if idx > 0:
        temp_report = report[:idx-1] + report[idx:]
        safe, _ = check_safety_report(temp_report)
        if safe:
            return True
    
    # Try removing the first element (direction might be wrong)
    if len(report) > 1:
        temp_report = report[1:]
        safe, _ = check_safety_report(temp_report)
        if safe:
            return True
    
    return False


if __name__ == "__main__":
    safe_count_part_1 = 0
    safe_count_part_2 = 0
    with open("input.txt", "r") as f:
        for line in f:
            report = list(map(int, line.split()))
            safe, idx = check_safety_report(report)
            if safe:
                safe_count_part_1 += 1
                safe_count_part_2 += 1
            elif check_safety_with_dampener(report, idx):
                safe_count_part_2 += 1

    print(safe_count_part_1)
    print(safe_count_part_2)
