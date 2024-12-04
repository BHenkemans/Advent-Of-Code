import fileinput


def read_file() -> [str]:
    return [line.rstrip('\n') for line in fileinput.input()]


def part1(lines: [str]) -> int:
    res = 0
    for line in lines:
        nums: [int] = []
        for c in line:
            if c.isnumeric():
                nums.append(int(c))
        res += nums[0] * 10 + nums[-1]

    return res

def map_str_to_num(text: str) -> int | bool:
    if text.startswith("one"):
        return 1
    elif text.startswith("two"):
        return 2
    elif text.startswith("three"):
        return 3
    elif text.startswith("four"):
        return 4
    elif text.startswith("five"):
        return 5
    elif text.startswith("six"):
        return 6
    elif text.startswith("seven"):
        return 7
    elif text.startswith("eight"):
        return 8
    elif text.startswith("nine"):
        return 9
    else:
        return False

def part2(lines: [str]) -> int:
    res = 0
    for line in lines:
        nums: [int] = []
        for cnt, c in enumerate(line):
            if c.isnumeric():
                nums.append(int(c))
                continue
            num = map_str_to_num(line[cnt:])
            if num:
                nums.append(num)
        res += nums[0] * 10 + nums[-1]
    return res


if __name__ == '__main__':
    lines = read_file()
    result_part1 = part1(lines)
    result_part2 = part2(lines)
    print(f"The result for part 1 is {result_part1}")
    print(f"The result for part 2 is {result_part2}")
