import fileinput

def read_file() -> [str]:
    return [line.rstrip('\n') for line in fileinput.input()]

#Ascending or descending
is_sorted = lambda r: all(r[i] <= r[i+1] for i in range(len(r) - 1)) or all(r[i] >= r[i+1] for i in range(len(r) - 1))

#Check if the gap is okay
okay_gap = lambda r: all(1 <= abs(r[i] - r[i+1]) <= 3  for i in range(len(r) - 1))

def part1(lines: [str]) -> int:
    report_status = 0
    for report_id, report  in enumerate(lines):
        report = [int(r) for r in report.split()]
        report_status += (is_sorted(report) and okay_gap(report))
    return report_status



def part2(lines: [str]) -> int:
    report_status = 0
    for report_id, report  in enumerate(lines):
        report = [int(r) for r in report.split()]
        if is_sorted(report) and okay_gap(report):
            report_status += 1
        else:
            for i in range(len(report)):
                left_side = report[:i]
                right_side = report[i+1:]
                new_report = left_side + right_side
                if is_sorted(new_report) and okay_gap(new_report):
                    report_status += 1
                    break

    return report_status


if __name__ == '__main__':
    lines = read_file()
    result_part1 = part1(lines)
    result_part2 = part2(lines)
    print(f"The result for part 1 is {result_part1}")
    print(f"The result for part 2 is {result_part2}")
