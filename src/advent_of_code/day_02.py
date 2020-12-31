from typing import Set, Tuple, Callable
from pathlib import Path


def parse_rule(rule: str) -> Tuple[str, int, int]:
    numbers, letter = rule.split(' ')
    first, second = numbers.split('-')
    return letter, int(first), int(second)


def is_valid_by_count(rule: str, password: str) -> bool:
    letter, min_occ, max_occ = parse_rule(rule)
    return password.count(letter) in range(min_occ, max_occ + 1)


def is_valid_by_existence(rule: str, password: str) -> bool:
    letter, first_occ, second_occ = parse_rule(rule)
    return (password[first_occ - 1] == letter) != (password[second_occ - 1] == letter)


def get_valid_count(password_entries: Set[Tuple[str]], is_valid: Callable) -> int:
    return len([entry for entry in password_entries if is_valid(*entry)])


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_02.txt'):
    with open(file_path) as f:
        password_entries = {tuple(line.strip().split(': ')) for line in f.readlines()}
    print(f'valid by count: {get_valid_count(password_entries, is_valid_by_count)}')
    print(f'valid by existence: {get_valid_count(password_entries, is_valid_by_existence)}')


if __name__ == '__main__':
    main()
