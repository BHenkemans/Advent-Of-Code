use day_01::process_part1;
use day_01::parse_list;
use std::fs;

fn main() {
    let file = fs::read_to_string("input.txt").unwrap();
    let (list1, list2) = parse_list(&file);
    println!("{}", process_part1(list1, list2));
}