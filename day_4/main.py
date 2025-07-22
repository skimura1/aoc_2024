from collections import defaultdict

def read_input():
    with open('./input.txt', 'r') as f:
        puzzle_input = f.read().strip().splitlines()
        return [list(row) for row in puzzle_input]


def check_xmas(grid: list[list[str]]) -> int:
    keyword = "XMAS"
    target_length = len(keyword)
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def is_valid_direction(row, col, dr, dc):
        for i in range(target_length):
            r = row + i * dr
            c = col + i * dc
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != keyword[i]:
                return False
        return True
 

    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                if is_valid_direction(row, col, dr, dc):
                    count += 1

    return count


def check_x_mas(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] != "A":
                continue
            corners = [grid[r - 1][c - 1], grid[r - 1][c + 1], grid[r + 1][c + 1], grid[r + 1][c - 1]]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                count += 1

    return count


# When X is encounterd, we check surrounding characters if there is an M, then in that direction of M, we check if A and S exist
if __name__ == "__main__":
    input = read_input()
    result_1 = check_xmas(input)
    result_2 = check_x_mas(input)
    print(result_1)
    print(result_2)
