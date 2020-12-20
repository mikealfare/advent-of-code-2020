from typing import List
from itertools import permutations


def sum_exists(port_numbers: List[int], port_sum: int) -> bool:
    potential_sums = {sum(sum_parts) for sum_parts in permutations(port_numbers, 2)}
    return port_sum in potential_sums


def find_first_error(port_numbers: List[int], preamble: int) -> int:
    for element in range(preamble, len(port_numbers)):
        if not sum_exists(port_numbers[element-preamble:element], port_numbers[element]):
            return port_numbers[element]


def find_contiguous_numbers_adding_to_provided_sum(port_numbers: List[int], target_sum: int) -> List[int]:
    for element in range(len(port_numbers)):
        this_subset = []
        subset_length = 2
        while sum(this_subset) < target_sum:
            this_subset = port_numbers[element:element + subset_length]
            subset_length += 1
        if sum(this_subset) == target_sum:
            return this_subset


def main():
    with open('input_files/day_09.txt') as f:
        port_numbers = [int(line.strip().replace('\n', '')) for line in f.readlines()]
    first_error = find_first_error(port_numbers, 25)
    print(f'the first error exists at {first_error}')
    contiguous_subset = find_contiguous_numbers_adding_to_provided_sum(port_numbers, first_error)
    print(f'the sum of the min and max of the subset is {min(contiguous_subset) + max(contiguous_subset)}')


if __name__ == '__main__':
    main()
