from typing import List, Tuple
from dataclasses import dataclass


@dataclass
class Move:
    direction: str

    DIRECTIONS = {
        'e': (2, 0),
        'se': (1, -1),
        'sw': (-1, -1),
        'w': (-2, 0),
        'ne': (1, 1),
        'nw': (-1, 1)
    }

    @property
    def x(self) -> int:
        return self.DIRECTIONS[self.direction][0]

    @property
    def y(self) -> int:
        return self.DIRECTIONS[self.direction][1]


Tile = Tuple[int, int]
Path = List[str]


def step(starting_tile: Tile, direction: str) -> Tile:
    move = Move(direction)
    return starting_tile[0] + move.x, starting_tile[1] + move.y


def find_end_of_path(tile_path: List[str]) -> Tile:
    tile = 0, 0
    for each_step in tile_path:
        tile = step(tile, each_step)
    return tile


def get_black_tiles(tile_paths: List[str]) -> List[Tile]:
    pass


def parse_path(path: str) -> Path:
    directions = []
    for direction in path.split():
        diagonal_direction = ''
        if not diagonal_direction and direction in ['e', 'w']:
            directions.append(direction)
        elif direction in ['n', 's']:
            diagonal_direction = direction
        elif diagonal_direction and direction in ['e', 'w']:
            directions.append(diagonal_direction + direction)
        else:
            raise ValueError('ERROR - unexpected direction sequence')
    return directions


def main():
    pass


if __name__ == '__main__':
    main()
