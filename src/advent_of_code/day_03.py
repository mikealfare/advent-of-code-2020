from typing import List

TREE = '#'
NO_TREE = '.'


class Map:

    def __init__(self, map_string: str):
        rows_as_strings = map_string.split('\n')
        self.rows = [
            [1 if point == TREE else 0 for point in row]
            for row in rows_as_strings
        ]
        self.width = len(self.rows[0])
        self.height = len(self.rows)

    def is_tree(self, row: int, column: int) -> bool:
        row_index = row - 1
        column_index = (column - 1) % self.width
        return self.rows[row_index][column_index] == 1

    def get_path_map(self, row_step: int, column_step: int) -> List[int]:
        path_map = []
        row = 1 + row_step
        column = 1 + column_step
        while row <= self.height:
            path_map.append(self.is_tree(row, column))
            row += row_step
            column += column_step
        return path_map

    def get_trees_in_path_map(self, row_step: int, column_step: int) -> int:
        path_map = self.get_path_map(row_step=row_step, column_step=column_step)
        return sum(path_map)

    def print(self):
        for row in self.rows:
            print(row)


if __name__ == '__main__':
    with open('input_files/day_03.txt') as f:
        map_file = f.read()
    tree_map = Map(map_file)
    print(f'1 right, 1 down encounters {tree_map.get_trees_in_path_map(row_step=1, column_step=1)} trees')
    print(f'3 right, 1 down encounters {tree_map.get_trees_in_path_map(row_step=1, column_step=3)} trees')
    print(f'5 right, 1 down encounters {tree_map.get_trees_in_path_map(row_step=1, column_step=5)} trees')
    print(f'7 right, 1 down encounters {tree_map.get_trees_in_path_map(row_step=1, column_step=7)} trees')
    print(f'1 right, 2 down encounters {tree_map.get_trees_in_path_map(row_step=2, column_step=1)} trees')
    product = (
            tree_map.get_trees_in_path_map(row_step=1, column_step=1) *
            tree_map.get_trees_in_path_map(row_step=1, column_step=3) *
            tree_map.get_trees_in_path_map(row_step=1, column_step=5) *
            tree_map.get_trees_in_path_map(row_step=1, column_step=7) *
            tree_map.get_trees_in_path_map(row_step=2, column_step=1)
    )
    print(f'product = {product}')
