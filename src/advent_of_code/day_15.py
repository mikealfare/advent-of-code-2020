from typing import List, Dict


def get_last_seen_dict(starting_numbers: List[int]) -> Dict[int, int]:
    last_seen = {}
    for turn, number in enumerate(starting_numbers[:-1]):
        last_seen.update({number: turn})
    return last_seen


def update_with_the_next_number(numbers: List[int], last_seen: Dict[int, int]):
    last_number = numbers[-1]
    last_index = len(numbers) - 1
    if last_number not in last_seen:
        next_number = 0
    else:
        next_number = last_index - last_seen[last_number]
    last_seen.update({last_number: last_index})
    numbers.append(next_number)


def get_nth_number(starting_numbers: List[int], position: int) -> int:
    numbers = starting_numbers.copy()
    last_seen = get_last_seen_dict(numbers)
    for i in range(len(numbers), position):
        update_with_the_next_number(numbers, last_seen)
    return numbers[-1]


def main():
    starting_numbers = [8, 11, 0, 19, 1, 2]
    print(f'the 2020th number will be {get_nth_number(starting_numbers, 2000)}')
    print(f'the 30000000th number will be {get_nth_number(starting_numbers, 30000000)}')


if __name__ == '__main__':
    main()
