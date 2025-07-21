def check_xmas(array: list[list[str]], col: int, row: int) -> int:
    neighbors = []
    rows = len(array)
    cols = len(array[0])
    count = 0
    left, right = 1, 1

    directions = [
        (left, right),
        (left, -right),
        (-left, right),
        (-left, -right),
        (0, right),
        (left, 0),
        (0, -right),
        (-left, 0),
    ]

    for dr, dc in directions:
        substring = []
        for i in range(4):
            r, c = row + (dr * i), col + (dc * i)
            if 0 <= r < rows and 0 <= c < cols:
                substring.append(array[r][c])
        word = "".join(substring)
        neighbors.append(word)

    for neighbor in neighbors:
        if neighbor == "XMAS":
            count += 1

    return count


# When X is encounterd, we check surrounding characters if there is an M, then in that direction of M, we check if A and S exist
if __name__ == "__main__":
    count_part_1 = 0

    input_array = []
    with open("input.txt", "r") as f:
        for line in f:
            input_array.append(list(line.strip()))

        for x, _ in enumerate(input_array):
            for y, y_char in enumerate(input_array[0]):
                if y_char == "X":
                    count_part_1 += check_xmas(input_array, x, y)

    print(count_part_1)
