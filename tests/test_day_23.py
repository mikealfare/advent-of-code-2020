from typing import List

import pytest

from tests.conftest import day_23


@pytest.mark.parametrize('cup_labels,current_cup,expected_cup_labels,expected_next_cup', [
    ([3, 8, 9, 1, 2, 5, 4, 6, 7], 3, [3, 2, 8, 9, 1, 5, 4, 6, 7], 2),
    ([3, 2, 8, 9, 1, 5, 4, 6, 7], 2, [3, 2, 5, 4, 6, 7, 8, 9, 1], 5),
    ([3, 2, 5, 4, 6, 7, 8, 9, 1], 5, [3, 4, 6, 7, 2, 5, 8, 9, 1], 8),
    ([3, 4, 6, 7, 2, 5, 8, 9, 1], 8, [4, 6, 7, 9, 1, 3, 2, 5, 8], 4),
    ([4, 6, 7, 9, 1, 3, 2, 5, 8], 4, [4, 1, 3, 6, 7, 9, 2, 5, 8], 1),
    ([4, 1, 3, 6, 7, 9, 2, 5, 8], 1, [4, 1, 9, 3, 6, 7, 2, 5, 8], 9),
    ([4, 1, 9, 3, 6, 7, 2, 5, 8], 9, [4, 1, 9, 2, 5, 8, 3, 6, 7], 2),
    ([4, 1, 9, 2, 5, 8, 3, 6, 7], 2, [4, 1, 5, 8, 3, 9, 2, 6, 7], 6),
    ([4, 1, 5, 8, 3, 9, 2, 6, 7], 6, [5, 7, 4, 1, 8, 3, 9, 2, 6], 5),
    ([5, 7, 4, 1, 8, 3, 9, 2, 6], 5, [5, 8, 3, 7, 4, 1, 9, 2, 6], 8)
])
def test_play_move(
        cup_labels: List[day_23.Cup],
        current_cup: day_23.Cup,
        expected_cup_labels: List[day_23.Cup],
        expected_next_cup: day_23.Cup
):
    cups = day_23.create_cups_dict(cup_labels)
    expected_cups = day_23.create_cups_dict(expected_cup_labels)
    assert day_23.play_move(cups, current_cup) == expected_next_cup
    assert cups == expected_cups
