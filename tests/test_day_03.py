from tests.conftest import day_03


sample_map_string = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''


def test_print():
    tree_map = day_03.Map(sample_map_string)
    tree_map.print()
    assert tree_map.width == 11
    assert tree_map.height == 11


def test_get_path_map():
    tree_map = day_03.Map(sample_map_string)
    path_map = tree_map.get_path_map(row_step=1, column_step=3)
    expected_path_map = [0, 1, 0, 1, 1, 0, 1, 1, 1, 1]
    assert path_map == expected_path_map


def test_get_trees_in_path_map():
    tree_map = day_03.Map(sample_map_string)
    assert tree_map.get_trees_in_path_map(row_step=1, column_step=3) == 7
