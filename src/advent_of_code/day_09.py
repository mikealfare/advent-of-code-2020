from typing import List
from itertools import combinations
from pathlib import Path


PortNumber = int


def find_first_error(port_numbers: List[PortNumber], preamble: int) -> PortNumber:
    for index, port_number in enumerate(port_numbers):
        if index < preamble:
            continue
        preamble_subset = port_numbers[index - preamble:index]
        preamble_sums = {sum(sum_parts) for sum_parts in combinations(preamble_subset, 2)}
        if port_number not in preamble_sums:
            return port_number


def find_contiguous_numbers_adding_to_target_sum(port_numbers: List[PortNumber], target_sum: int) -> List[PortNumber]:
    for index in range(len(port_numbers)):
        this_subset = []
        while sum(this_subset) < target_sum or len(this_subset) < 2:
            this_subset.append(port_numbers[index + len(this_subset)])
        if sum(this_subset) == target_sum:
            return this_subset


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_09.txt'):
    with open(file_path) as f:
        port_numbers = [int(line.strip()) for line in f.readlines()]
    first_error = find_first_error(port_numbers, 25)
    print(f'the first error occurs at {first_error}')
    contiguous_subset = find_contiguous_numbers_adding_to_target_sum(port_numbers, first_error)
    print(f'the sum of the min and max of the subset is {min(contiguous_subset) + max(contiguous_subset)}')


if __name__ == '__main__':
    main()
