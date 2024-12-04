import fileinput


def read_file() -> [[str]]:
    return [[c for c in line.rstrip('\n')] for line in fileinput.input()]


def part1(grid: [[str]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for row in range(rows):
        for col in range(cols):
            for diff_row, diff_col in directions:
                res += detect_word(grid, row, col, (diff_row, diff_col), "XMAS")
    return res

def detect_word(grid: [[str]], r: int, c: int, dir: (int, int), target_word: str) -> bool:
    word = ""
    for _ in range(len(target_word)):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            word += grid[r][c]
        else:
            break
        r += dir[0]
        c += dir[1]
    if word == target_word:
        return True
    return False


def part2(grid: [[str]]) -> int:
    res = 0
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if detect_word(grid, r, c, (1,1), "MAS") \
                    or detect_word(grid, r+2, c+2, (-1,-1), "MAS"):
                res += detect_word(grid, r+2, c, (-1,1), "MAS") \
                       or detect_word(grid, r, c+2, (1,-1), "MAS")

    return res
if __name__ == '__main__':
    lines = read_file()
    result_part1 = part1(lines)
    result_part2 = part2(lines)
    print(f"The result for part 1 is {result_part1}")
    print(f"The result for part 2 is {result_part2}")
