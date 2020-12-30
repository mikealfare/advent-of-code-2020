from typing import List, Tuple

import pytest

from tests.conftest import day_10

small_example = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
large_example = [
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
]


@pytest.mark.parametrize('adaptors,expected', [
    (small_example, [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]),
    (large_example, [1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 1, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 1, 1, 1, 1, 3])
])
def test_get_joltage_differences(adaptors: List[day_10.Adaptor], expected: List[int]):
    assert  day_10.get_joltage_differences(adaptors) == expected


@pytest.mark.parametrize('adaptors,expected', [
    (small_example, (7, 0, 5)),
    (large_example, (22, 0, 10))
])
def test_get_joltage_difference_distribution(adaptors: List[day_10.Adaptor], expected: Tuple[int, int, int]):
    distribution = day_10.get_joltage_difference_distribution(adaptors)
    assert (distribution[1], distribution[2], distribution[3]) == expected


@pytest.mark.parametrize('joltage_differences,expected', [
    ([], 1),
    ([1], 1),
    ([2], 1),
    ([1, 1], 2),
    ([1, 2], 2),
    ([2, 1], 2),
    ([1, 1, 1], 4),
    ([1, 1, 2], 3),
    ([2, 1, 1], 3),
    ([1, 2, 1], 3),
    ([1, 1, 1, 1], 7),
    ([1, 1, 1, 2], 6),
    ([2, 1, 1, 1], 6),
    ([1, 1, 2, 1], 5),
    ([1, 2, 1, 1], 5),
    ([1, 2, 1, 2], 5),
    ([1, 1, 1, 1, 1], 13),
    (day_10.get_joltage_differences(small_example), 8),
    (day_10.get_joltage_differences(large_example), 19208)
])
def test_get_valid_adaptor_combinations(joltage_differences: List[int], expected: int):
    assert day_10.get_valid_adaptor_combinations(joltage_differences) == expected
