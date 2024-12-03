pub fn process_part1 (input: &str) -> i32 {
    input.lines()
        .map(|line| {
            let report: Vec<i32> = line.split_whitespace()
                .map(|val| val.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
            let mut reversed_report: Vec<i32> = report.clone();
            reversed_report.reverse();
            (report.is_sorted() || reversed_report.is_sorted()) && diff_rule(report)
        }).map(|b| if b { 1 } else { 0 }).sum::<i32>()
}

fn diff_rule (report: Vec<i32>) -> bool {
    for i in 0..(report.len() - 1) {
        let diff: i32 = (report[i] - report[i + 1]).abs();
        if diff < 1 || diff > 3 {
            return false;
        }
    }
    true
}

pub fn process_part2(input: &str) -> i32 {
    input.lines()
        .map(|line| {
            let mut report: Vec<i32> = line.split_whitespace()
                .map(|val| val.parse::<i32>().unwrap())
                .collect::<Vec<i32>>();
            for i in 0..report.len() {
                let save_val: i32 = report[i];
                report.remove(i);

                let mut reversed_report: Vec<i32> = report.clone();
                reversed_report.reverse();

                if (report.is_sorted() || reversed_report.is_sorted()) && diff_rule(report.clone()) {
                    return true;
                }
                report.insert(i, save_val);

            }
            false
        }).map(|b| if b { 1 } else { 0 }).sum::<i32>()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part1() {
        let input: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";
        let result = process_part1(input);
        assert_eq!(result, 2);
    }
    #[test]
    fn part2() {
        let input: &str = "7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9";
        let result = process_part2(input);
        assert_eq!(result, 4);
    }
}
