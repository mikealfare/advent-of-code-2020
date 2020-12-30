from typing import List
from collections import Counter
from copy import deepcopy
from pathlib import Path


Adaptor = int


def get_joltage_differences(adaptors: List[Adaptor]) -> List[int]:
    ordered_adaptors = deepcopy(adaptors)
    ordered_adaptors.extend([0, max(adaptors) + 3])
    ordered_adaptors.sort()
    differences = [this - previous for this, previous in zip(ordered_adaptors[1:], ordered_adaptors[:-1])]
    return differences


def get_joltage_difference_distribution(adaptors: List[Adaptor]) -> Counter:
    joltage_differences = get_joltage_differences(adaptors)
    return Counter(joltage_differences)


def get_valid_adaptor_combinations(joltage_differences: List[int]) -> int:

    if 3 in joltage_differences:
        first_3 = joltage_differences.index(3)
        subset_before = joltage_differences[:first_3]
        subset_after = joltage_differences[first_3+1:]
        return get_valid_adaptor_combinations(subset_before) * get_valid_adaptor_combinations(subset_after)

    if len(joltage_differences) == 0:
        return 1
    if joltage_differences[0] > 3:
        return 0
    if len(joltage_differences) == 1:
        return 1

    remaining_differences_if_included = joltage_differences[1:]
    combinations_including_this_adaptor = get_valid_adaptor_combinations(remaining_differences_if_included)

    remaining_differences_if_excluded = joltage_differences[1:]
    remaining_differences_if_excluded[0] += joltage_differences[0]
    combinations_excluding_this_adaptor = get_valid_adaptor_combinations(remaining_differences_if_excluded)

    return combinations_including_this_adaptor + combinations_excluding_this_adaptor


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_10.txt'):
    with open(file_path) as f:
        adaptors = [int(line.strip()) for line in f.readlines()]
    joltage_distribution = get_joltage_difference_distribution(adaptors)
    print(f'1-jolt * 3-jolt is {joltage_distribution[1] * joltage_distribution[3]}')
    joltage_differences = get_joltage_differences(adaptors)
    adaptor_combinations = get_valid_adaptor_combinations(joltage_differences)
    print(f'there are {adaptor_combinations} combinations of adaptors that work')


if __name__ == '__main__':
    main()
