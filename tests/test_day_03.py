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


@pytest.mark.parametrize('tree_map,row,column,expected', [
    (sample_tree_map, 1, 3, True),
    (sample_tree_map, 2, 1, True),
    (sample_tree_map, 4, 11, True),
    (sample_tree_map, 1, 1, False),
    (sample_tree_map, 2, 2, False)
])
def test_is_tree(tree_map: day_03.TreeMap, row: int, column: int, expected: bool):
    assert day_03.is_tree(tree_map, row, column) == expected


@pytest.mark.parametrize('tree_map,row_step,column_step,expected', [
    (sample_tree_map, 1, 1, 2),
    (sample_tree_map, 1, 3, 7),
    (sample_tree_map, 1, 5, 3),
    (sample_tree_map, 1, 7, 4),
    (sample_tree_map, 2, 1, 2),
])
def test_get_tree_count_in_slope(tree_map: day_03.TreeMap, row_step: int, column_step: int, expected: int):
    assert day_03.get_tree_count_in_slope(tree_map, row_step, column_step) == expected
