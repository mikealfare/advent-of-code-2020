from typing import Tuple, List
from pathlib import Path


def parse_rule(rule: str) -> Tuple[str, int, int]:
    numbers, letter = rule.split(' ')
    first, second = numbers.split('-')
    return letter, int(first), int(second)


def is_valid_by_count(password: str, rule: str) -> bool:
    letter, min_occ, max_occ = parse_rule(rule)
    occurrences = password.count(letter)
    return occurrences in range(min_occ, max_occ + 1)


def is_valid_by_existence(password: str, rule: str) -> bool:
    letter, first_occ, second_occ = parse_rule(rule)
    first_index = first_occ - 1
    second_index = second_occ - 1
    return (password[first_index] == letter) != (password[second_index] == letter)


def get_valid_count_by_count(password_entries: List[str]) -> int:
    valid_count = 0
    for entry in password_entries:
        rule, password = entry.split(': ')
        if is_valid_by_count(password, rule):
            valid_count += 1
    return valid_count


def get_valid_count_by_existence(password_entries: List[str]) -> int:
    valid_count = 0
    for entry in password_entries:
        rule, password = entry.split(': ')
        if is_valid_by_existence(password, rule):
            valid_count += 1
    return valid_count


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_02.txt'):
    with open(file_path) as f:
        password_entries = [line.strip() for line in f.readlines()]
    valid_by_count = get_valid_count_by_count(password_entries)
    valid_by_existence = get_valid_count_by_existence(password_entries)
    print(f'valid by count: {valid_by_count}')
    print(f'valid by existence: {valid_by_existence}')


if __name__ == '__main__':
    main()
