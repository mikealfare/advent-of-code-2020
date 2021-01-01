from typing import List, Tuple

import pytest

from tests.conftest import day_03


sample_tree_map = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#'
]


@pytest.mark.parametrize('tree_map,slope,expected', [
    (sample_tree_map, (1, 1), 2),
    (sample_tree_map, (1, 3), 7),
    (sample_tree_map, (1, 5), 3),
    (sample_tree_map, (1, 7), 4),
    (sample_tree_map, (2, 1), 2),
])
def test_get_tree_count_in_slope(tree_map: List[str], slope: Tuple[int, int], expected: int):
    assert day_03.get_tree_count(tree_map, slope) == expected
