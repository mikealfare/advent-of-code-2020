import pytest

from tests.conftest import day_15


@pytest.mark.parametrize('starting_numbers,expected', [
    ([1, 3, 2], {1: 0, 3: 1}),
    ([2, 1, 3], {2: 0, 1: 1}),
    ([1, 2, 3], {1: 0, 2: 1}),
    ([2, 3, 1], {2: 0, 3: 1}),
    ([3, 2, 1], {3: 0, 2: 1}),
    ([3, 1, 2], {3: 0, 1: 1}),
    ([0, 3, 6], {0: 0, 3: 1})
])
def test_get_last_seen_dict(starting_numbers, expected):
    assert day_15.get_last_seen_dict(starting_numbers) == expected


@pytest.mark.parametrize('numbers,expected', [
    ([0, 3, 6, 0], 3),
    ([0, 3, 6, 0, 3], 3),
    ([1, 3, 2], 0),
    ([2, 1, 3], 0),
    ([1, 2, 3], 0),
    ([0, 3, 6], 0),
    ([0, 3, 6, 0, 3, 3], 1),
    ([0, 3, 6, 0, 3, 3, 1], 0),
    ([0, 3, 6, 0, 3, 3, 1, 0], 4),
    ([0, 3, 6, 0, 3, 3, 1, 0, 4], 0),
])
def test_get_next_number(numbers, expected):
    last_seen = day_15.get_last_seen_dict(numbers)
    assert day_15.get_next_number(last_seen, numbers[-1], len(numbers) - 1) == expected


@pytest.mark.parametrize('starting_numbers,position,expected', [
    ([0, 3, 6], 2020, 436),
    ([1, 3, 2], 2020, 1),
    ([2, 1, 3], 2020, 10),
    ([1, 2, 3], 2020, 27),
    ([2, 3, 1], 2020, 78),
    ([3, 2, 1], 2020, 438),
    ([3, 1, 2], 2020, 1836),
    ([0, 3, 6], 30000000, 175594),
#    ([1, 3, 2], 30000000, 2578),
#    ([2, 1, 3], 30000000, 3544142),
#    ([1, 2, 3], 30000000, 261214),
#    ([2, 3, 1], 30000000, 6895259),
#    ([3, 2, 1], 30000000, 18),
#    ([3, 1, 2], 30000000, 362)
])
def test_get_2020th_number(starting_numbers, position, expected):
    assert day_15.get_nth_number(starting_numbers, position) == expected
