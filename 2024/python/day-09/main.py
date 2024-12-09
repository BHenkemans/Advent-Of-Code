import fileinput


def read_file() -> [str]:
    return [line.rstrip('\n') for line in fileinput.input()][0]


def part1(line: str) -> int:
    res = 0
    disk_rep_list: [str] = []
    for cnt, c in enumerate(line):
        if not int(c) > 0:
            continue
        if not cnt % 2:
            for _ in range(int(c)):
                disk_rep_list.append(str(cnt//2))
        else:
            for _ in range(int(c)):
                disk_rep_list.append('.')
    # print(disk_rep_list)

    for i in range(len(disk_rep_list)):
        if disk_rep_list[i] != '.':
            continue
        for j in range(len(disk_rep_list)-1, i, -1):
            if disk_rep_list[j] == '.':
                continue
            disk_rep_list[i] = disk_rep_list[j]
            disk_rep_list[j] = '.'
            break

    for cnt, v in enumerate(disk_rep_list):
        if v.isnumeric():
            res += cnt*int(v)
    return res




def part2(line: str) -> int:
    res = 0
    disk_rep_list = []
    for cnt, c in enumerate(line):
        if not int(c) > 0:
            continue
        if not cnt % 2:
            disk_rep_list.append((int(c), str(cnt // 2)))
        else:
            disk_rep_list.append((int(c),'.'))

    for i in range(len(disk_rep_list)):
        if disk_rep_list[i][1] != '.':
            continue
        for j in range(len(disk_rep_list)-1, i, -1):
            if disk_rep_list[j][1] == '.':
                continue
            elif disk_rep_list[j][0] > disk_rep_list[i][0]:
                continue
            elif disk_rep_list[j][0] == disk_rep_list[i][0]:
                disk_rep_list[i] = disk_rep_list[j]
                disk_rep_list[j] = (disk_rep_list[i][0], '.')
            else:
                new_free_space = disk_rep_list[i][0] - disk_rep_list[j][0]
                disk_rep_list.insert(i, disk_rep_list[j])
                disk_rep_list[i+1] = (new_free_space, '.')
                disk_rep_list[j+1] = (disk_rep_list[i][0], '.')
            break
    str_rep = ''
    for space, val in disk_rep_list:
        if val == '.':
            str_rep += space * '.'
        else:
            str_rep += space * val

    cnt = 0
    for space, val in disk_rep_list:
        if val == '.':
            cnt += space
            continue
        for i in range(space):
            res += (cnt+i)*int(val)
        cnt += space
    return res


if __name__ == '__main__':
    line = read_file()
    result_part1 = part1(line)
    result_part2 = part2(line)
    print(f"The result for part 1 is {result_part1}")
    print(f"The result for part 2 is {result_part2}")
