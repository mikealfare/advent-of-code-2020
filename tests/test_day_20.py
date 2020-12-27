from pathlib import Path
from math import prod

import pytest

from tests.conftest import day_20


sample_solution = [
    [1951, 2311, 3079],
    [2729, 1427, 2473],
    [2971, 1489, 1171]
]


@pytest.fixture
def sample_tiles():
    return day_20.parse_input(Path(__file__).parent / 'static' / 'day_20.txt')


def test_parse_input(sample_tiles):
    print('Parsed tiles:')
    for tile in sample_tiles:
        print(str(tile))
    assert len(sample_tiles) == 9


def test_find_edges(sample_tiles):
    edge_tiles, corner_tiles = day_20.find_edges(sample_tiles)
    print('found these edge tiles')
    for tile, unmatched_values in edge_tiles.items():
        print(f'{tile}: has {unmatched_values} unmatched edges')
    print('found these corner tiles')
    for tile, unmatched_values in corner_tiles.items():
        print(f'{tile}: has {unmatched_values} two unmatched edges')
    assert len(edge_tiles) == 4
    assert len(corner_tiles) == 4


def test_find_corner_tiles(sample_tiles):
    _, corner_tiles = day_20.find_edges(sample_tiles)
    product_of_corner_tile_ids = prod([tile.tile_id for tile in corner_tiles])
    assert product_of_corner_tile_ids == prod([1951, 3079, 2971, 1171])
