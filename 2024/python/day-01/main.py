import fileinput
from collections import Counter


def read_file() -> ([int], [int]):
    list1, list2 = [], []
    for line in fileinput.input():
        line.rstrip('\n')
        v1, v2 = line.rsplit()
        list1.append(int(v1))
        list2.append(int(v2))
    list1.sort()
    list2.sort()
    return list1, list2


def part1(list1: [int], list2: [int]) -> int:
    res = 0
    for count, val in enumerate(list1):
        res += abs(val - list2[count])
    return res



def part2(list1: [int], list2: [int]) -> int:
    c1, c2 = Counter(list1), Counter(list2)
    res = 0
    for el in c1.elements():
        res += el * c2[el]
    return res


if __name__ == '__main__':
    list1, list2 = read_file()
    result_part1 = part1(list1, list2)
    result_part2 = part2(list1, list2)
    print(f"The result for part 1 is {result_part1}")
    print(f"The result for part 2 is {result_part2}")
