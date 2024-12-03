import fileinput
import re

def read_file() -> [str]:
    return [line.rstrip('\n') for line in fileinput.input()]


def part1(lines: [str]) -> int:
    r = r"mul\((\d+),(\d+)\)"
    res = 0
    matches = [match for line in lines for match in re.findall(r, line)]
    for match in matches:
        n, k = map(int, match)
        res += n*k
    return res



def part2(lines: [str]) -> int:
    r = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
    res = 0
    enabled = True
    matches = [match for line in lines for match in re.findall(r, line)]
    for match in matches:
        n, k, do_group, dont_group = match
        if do_group != "":
            enabled = True
        elif dont_group != "":
            enabled = False
        else:
            res += int(n) * int(k) * enabled
    return res


if __name__ == '__main__':
    lines = read_file()
    result_part1 = part1(lines)
    result_part2 = part2(lines)
    print(f"The result for part 1 is {result_part1}")
    print(f"The result for part 2 is {result_part2}")
