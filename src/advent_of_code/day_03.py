from typing import List, Tuple, Set
from pathlib import Path
from math import prod


def get_slope_squares(tree_map: List[str], slope: Tuple[int, int]) -> Set[Tuple[int, int]]:
    slope_rows, slope_columns = slope
    return {
        (row, slope_columns * step)
        for step, row in enumerate(range(0, len(tree_map), slope_rows))
    }


def is_tree(tree_map: List[str], square: Tuple[int, int]) -> bool:
    row, column = square
    row_of_trees = tree_map[row]
    return row_of_trees[column % len(row_of_trees)] == '#'


def get_tree_count(tree_map: List[str], slope: Tuple[int, int]) -> int:
    slope = get_slope_squares(tree_map, slope)
    trees = {square for square in slope if is_tree(tree_map, square)}
    return len(trees)


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_03.txt'):
    with open(file_path) as f:
        tree_map = [line.strip() for line in f.readlines()]
    print(f'3 right, 1 down encounters {get_tree_count(tree_map, (1, 3))} trees')
    product = prod([get_tree_count(tree_map, slope) for slope in {(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)}])
    print(f'the product of all trees encountered is {product}')


if __name__ == '__main__':
    main()
