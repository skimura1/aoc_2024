def part_1(report: list[int]):
    decreasing = False
    dampener = True
    if report[0] - report[-1] > 0:
        decreasing = True
    left = 0
    right = 1
    while right < len(report):
        prev = report[left]
        curr = report[right]
        diff = prev - curr
        bad_level = bad_level_check(decreasing, diff)

        if bad_level and dampener:
            right += 1
            dampener = False
            continue

        if bad_level and not dampener:
            return False

        left += 1
        right += 1

    return True


def bad_level_check(decreasing: bool, diff: int):
    if decreasing and (diff >= 1 and diff <= 3):
        return False
    elif not decreasing and (diff >= -3 and diff <= -1):
        return False

    return True


if __name__ == "__main__":
    safe_count = 0
    with open("input.txt", "r") as f:
        for line in f:
            if part_1(list(map(int, line.split()))):
                safe_count += 1

    print(safe_count)
