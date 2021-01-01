from typing import List, Dict


def get_last_seen_dict(numbers: List[int]) -> Dict[int, int]:
    last_seen = {}
    for turn, number in enumerate(numbers[:-1]):
        last_seen[number] = turn
    return last_seen


def get_next_number(last_seen: Dict[int, int], last_number: int, last_index: int) -> int:
    return last_index - last_seen.get(last_number, last_index)


def get_nth_number(starting_numbers: List[int], position: int) -> int:
    last_seen = get_last_seen_dict(starting_numbers)
    last_number = starting_numbers[-1]
    for index in range(len(starting_numbers), position):
        next_number = get_next_number(last_seen, last_number, index - 1)
        last_seen[last_number] = index - 1
        last_number = next_number
    return last_number


def main():
    starting_numbers = [8, 11, 0, 19, 1, 2]
    print(f'the 2020th number will be {get_nth_number(starting_numbers.copy(), 2000)}')
    print(f'the 30000000th number will be {get_nth_number(starting_numbers.copy(), 30000000)}')


if __name__ == '__main__':
    main()
