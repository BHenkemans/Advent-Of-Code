use std::iter::zip;

pub fn parse_list(input: &str) -> (Vec<i32>, Vec<i32>) {
    let (mut list1, mut list2): (Vec<_>, Vec<_>) = input.lines() /*Split on new lines*/
        .map(|line| {
            let mut parts = line.split_whitespace();  /*Split on spaces*/
            (
                parts
                    .next() /*Get next item*/
                    .unwrap() /*This will always work, our input is not mall-formed*/
                    .parse::<i32>() /*Get a number*/
                    .unwrap(), /*This will always work*/
                /*Again!*/
                parts
                    .next()
                    .unwrap()
                    .parse::<i32>()
                    .unwrap(),
            )
        })
        .unzip();
    list1.sort(); /*Sort it*/
    list2.sort();
    (list1, list2) /*Return it!*/
}
pub fn process_part1(list1: Vec<i32>, list2: Vec<i32>) -> i32 {
    zip(list1, list2) /*Iterate over both lists simultaneously*/
        .map(|(el1, el2)| (el1-el2).abs()) /*Compute absolute difference*/
        .sum() /*Result time*/
}

pub fn process_part2(list1: Vec<i32>, list2: Vec<i32>) -> i32 {
    list1.iter()/*Go over the left list*/
        .map(|el1|
            el1 * list2.iter() /*Multiply by the count*/
                .filter(|&el2| *el1 == *el2).count() as i32) /*Count*/
        .sum() /*Result time*/
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse() {
        let input: &str = "3   4
4   3
2   5
1   3
3   9
3   3";
        let (list1, list2) = parse_list(input);
        assert_eq!(list1, [1, 2, 3, 3, 3, 4]);
        assert_eq!(list2, [3, 3, 3, 4, 5, 9]);
    }

    #[test]
    fn part1_base_case() {
        let input: &str = "3   4
4   3
2   5
1   3
3   9
3   3";
        let (list1, list2) = parse_list(input);
        let result:i32 = process_part1(list1, list2);
        assert_eq!(result, 11);
    }

    #[test]
    fn part2_base_case() {
    let input: &str = "3   4
4   3
2   5
1   3
3   9
3   3";
    let (list1, list2) = parse_list(input);
    let result:i32 = process_part2(list1, list2);
    assert_eq!(result, 31);
}
}
