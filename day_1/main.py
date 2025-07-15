from collections import Counter


def part_1(col1: list[int], col2: list[int]) -> int:
    sum = 0
    sorted_col1 = sorted(col1)
    sorted_col2 = sorted(col2)
    for i in range(len(col1)):
        sum += abs(sorted_col1[i] - sorted_col2[i])

    return sum


def part_2(items_to_count: list[int], items: list[int]) -> int:
    sum = 0

    item_counts = Counter(items)
    unique_items_to_count = set(items_to_count)
    filtered_count = {item: item_counts[item] for item in unique_items_to_count}

    for num in items_to_count:
        sum += num * filtered_count[num]

    return sum


if __name__ == "__main__":
    col1 = []
    col2 = []
    sum_1 = 0
    sum_2 = 0

    with open("input.txt", "r") as f:
        for line in f:
            a, b = map(int, line.strip().split())
            col1.append(a)
            col2.append(b)

    sum_1 += part_1(col1, col2)
    sum_2 += part_2(col1, col2)

    print(sum_1)
    print(sum_2)
