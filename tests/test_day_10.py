import pytest

from tests.conftest import day_10

small_example = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
small_expected_distribution = (7, 0, 5)
small_expected_adaptor_paths = 8


large_example = [
    28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19,
    38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3
]
large_expected_distribution = (22, 0, 10)
large_expected_adaptor_paths = 19208


@pytest.mark.parametrize('adaptors,expected', [
    (small_example, [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]),
    (large_example, [])
])
def test_get_joltage_differences(adaptors, expected):
    assert  day_10.get_joltage_differences(adaptors) == expected


@pytest.mark.parametrize('adaptors,expected', [
    (small_example, small_expected_distribution),
    (large_example, large_expected_distribution)
])
def test_get_joltage_difference_distribution(adaptors, expected):
    distribution = day_10.get_joltage_difference_distribution(adaptors)
    assert distribution[1] == expected[0]
    assert distribution[2] == expected[1]
    assert distribution[3] == expected[2]


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
    ([1, 1, 1, 1, 1], 13)
])
def test_get_valid_adaptor_combinations(joltage_differences, expected):
    assert day_10.get_valid_adaptor_combinations(joltage_differences) == expected


@pytest.mark.parametrize('adaptors,expected', [
    (small_example, small_expected_adaptor_paths),
    (large_example, large_expected_adaptor_paths)
])
def test_get_valid_adaptor_combinations(adaptors, expected):
    joltage_differences = day_10.get_joltage_differences(adaptors)
    assert day_10.get_valid_adaptor_combinations(joltage_differences) == expected
