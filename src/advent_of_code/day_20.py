from typing import Dict, List, Set, Tuple
from copy import deepcopy
from math import prod


class Tile:

    def __init__(self, tile_id: int, tile_definition: List[str]):
        self.tile_id = tile_id
        self.size = len(tile_definition)
        self.top = tile_definition[0]
        self.bottom = tile_definition[-1]
        self.left = ''.join([tile_string[0] for tile_string in tile_definition])
        self.right = ''.join([tile_string[self.size - 1] for tile_string in tile_definition])

    @property
    def all_possible_sides(self) -> Set[str]:
        return {
            self.top,
            self.bottom,
            self.left,
            self.right,
            self.top[::-1],
            self.bottom[::-1],
            self.left[::-1],
            self.right[::-1]
        }

    def rotate_left(self):
        self.top, self.bottom, self.left, self.right = (
            self.right,
            self.left,
            self.top[::-1],
            self.bottom[::-1]
        )

    def rotate_halfway(self):
        self.rotate_left()  # R, L -T, -B
        self.rotate_left()  # -B, -T, -R, -L

    def rotate_right(self):
        self.top, self.bottom, self.left, self.right = (
            self.left[::-1],
            self.right[::-1],
            self.bottom,
            self.top
        )

    def flip_top_to_bottom(self):
        self.top, self.bottom, self.left, self.right = (
            self.bottom,
            self.top,
            self.left[::-1],
            self.right[::-1]
        )

    def flip_left_to_right(self):
        self.top, self.bottom, self.left, self.right = (
            self.top[::-1],
            self.bottom[::-1],
            self.right,
            self.left
        )

    def __eq__(self, other):
        return self.tile_id == other.tile_id

    def __str__(self):
        return f'ID: {self.tile_id} - top, bottom, left, right = {self.top}, {self.bottom}, {self.left}, {self.right}'

    def __hash__(self):
        return self.tile_id


def find_edges(tiles: List[Tile]) -> Tuple[Dict[Tile, int], Dict[Tile, int]]:
    tiles_to_check = deepcopy(tiles)
    edge_tiles = {}
    corner_tiles = {}
    for this_tile in tiles:
        possible_sides = set()
        for tile in tiles_to_check:
            if tile != this_tile:
                possible_sides = possible_sides.union(tile.all_possible_sides)
        unmatched_edges = this_tile.all_possible_sides - possible_sides
        if len(unmatched_edges) == 2:
            edge_tiles.update({this_tile: len(unmatched_edges)})
        if len(unmatched_edges) == 4:
            corner_tiles.update({this_tile: len(unmatched_edges)})
    return edge_tiles, corner_tiles


def parse_input(file_name: str = 'input_files/day_20.txt') -> List[Tile]:
    with open(file_name) as f:
        lines = [line.strip() for line in f.readlines()]
    tiles = {}
    tile_id = 0
    for line in lines:
        if line.startswith('Tile'):
            tile_id = int(line.split(' ')[1].strip(':'))
            tiles.update({tile_id: []})
        elif '#' in line or '.' in line:
            tiles[tile_id].append(line)
    return [Tile(tile_id, tile_definition) for tile_id, tile_definition in tiles.items()]


def main():
    tiles = parse_input()
    _, corner_tiles = find_edges(tiles)
    prod_of_corner_ids = prod([tile.tile_id for tile in corner_tiles])
    print(f'the product of the corner tiles is {prod_of_corner_ids}')


if __name__ == '__main__':
    main()
