from typing import List
from pathlib import Path


TreeMap = List[str]


def is_tree(tree_map: TreeMap, row: int, column: int) -> bool:
    tree_row = tree_map[row - 1]
    column_index = (column - 1) % len(tree_row)
    return tree_row[column_index] == '#'


def get_tree_count_in_slope(tree_map: TreeMap, row_step: int, column_step: int) -> int:
    tree_count = 0
    row = 1 + row_step
    column = 1 + column_step
    while row <= len(tree_map):
        if is_tree(tree_map, row, column):
            tree_count += 1
        row += row_step
        column += column_step
    return tree_count


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_03.txt'):
    with open(file_path) as f:
        tree_map = [line.strip() for line in f.readlines()]
    print(f'3 right, 1 down encounters {get_tree_count_in_slope(tree_map, 1, 3)} trees')
    product = (
            get_tree_count_in_slope(tree_map, 1, 1) *
            get_tree_count_in_slope(tree_map, 1, 3) *
            get_tree_count_in_slope(tree_map, 1, 5) *
            get_tree_count_in_slope(tree_map, 1, 7) *
            get_tree_count_in_slope(tree_map, 2, 1)
    )
    print(f'the product of all trees encountered is {product}')


if __name__ == '__main__':
    main()
