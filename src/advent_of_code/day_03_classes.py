from dataclasses import dataclass
from typing import List, Tuple
from pathlib import Path
from operator import add
from math import prod


@dataclass
class TreeMap:
    tile: List[str]

    def is_tree(self, square: Tuple[int, int]) -> bool:
        row, column = square
        row_of_trees = self.tile[row]
        return row_of_trees[column % len(row_of_trees)] == '#'

    def get_tree_count(self, slope: Tuple[int, int]) -> int:
        tree_count = 0
        square = 0, 0
        while square in self:
            if self.is_tree(square):
                tree_count += 1
            square = tuple(map(add, square, slope))
        return tree_count

    def __contains__(self, item: Tuple[int, int]) -> bool:
        row, column = item
        return row in range(len(self.tile)) and column >= 0


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_03.txt'):
    with open(file_path) as f:
        tree_map = TreeMap([line.strip() for line in f.readlines()])
    print(f'3 right, 1 down encounters {tree_map.get_tree_count((1, 3))} trees')
    product = prod([tree_map.get_tree_count(slope) for slope in {(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)}])
    print(f'the product of all trees encountered is {product}')


if __name__ == '__main__':
    main()
