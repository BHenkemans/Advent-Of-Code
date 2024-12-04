import fileinput
from typing import Dict, Any


def read_file() -> [str]:
    return [line.rstrip('\n') for line in fileinput.input()]


def part1(lines: [str]) -> int:
    MAX_MAP = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    res = 0
    for line in lines:
        valid = True
        game, rounds = line.split(":")
        _, gameid = game.split()
        draws = [[a.strip().split() for a in a.split(",")] for a in rounds.split(";")]
        for draw in draws:
            for amount, colour in draw:
                if MAX_MAP[colour] < int(amount):
                    valid = False
        if valid:
            res += int(gameid)
    return res



def part2(lines: [str]) -> int:
    res = 0
    for line in lines:
        MAX_MAP: dict[str | Any, int] = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        _, rounds = line.split(":")
        draws = [[a.strip().split() for a in a.split(",")] for a in rounds.split(";")]
        for draw in draws:
            for amount, colour in draw:
                if int(amount) > MAX_MAP[colour]:
                    MAX_MAP[colour] = int(amount)
        res += MAX_MAP['red'] * MAX_MAP['blue'] * MAX_MAP['green']
    return res


if __name__ == '__main__':
    lines = read_file()
    result_part1 = part1(lines)
    result_part2 = part2(lines)
    print(f"The result for part 1 is {result_part1}")
    print(f"The result for part 2 is {result_part2}")
