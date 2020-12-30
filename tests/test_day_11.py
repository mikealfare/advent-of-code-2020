from typing import List

import pytest

from tests.conftest import day_11


sample_layout_0 = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL'
]
sample_layout_1 = [
    '#.##.##.##',
    '#######.##',
    '#.#.#..#..',
    '####.##.##',
    '#.##.##.##',
    '#.#####.##',
    '..#.#.....',
    '##########',
    '#.######.#',
    '#.#####.##'
]
sample_layout_2 = [
    '#.LL.L#.##',
    '#LLLLLL.L#',
    'L.L.L..L..',
    '#LLL.LL.L#',
    '#.LL.LL.LL',
    '#.LLLL#.##',
    '..L.L.....',
    '#LLLLLLLL#',
    '#.LLLLLL.L',
    '#.#LLLL.##'
]
sample_layout_3 = [
    '#.##.L#.##',
    '#L###LL.L#',
    'L.#.#..#..',
    '#L##.##.L#',
    '#.##.LL.LL',
    '#.###L#.##',
    '..#.#.....',
    '#L######L#',
    '#.LL###L.L',
    '#.#L###.##'
]
sample_layout_4 = [
    '#.#L.L#.##',
    '#LLL#LL.L#',
    'L.L.L..#..',
    '#LLL.##.L#',
    '#.LL.LL.LL',
    '#.LL#L#.##',
    '..L.L.....',
    '#L#LLLL#L#',
    '#.LLLLLL.L',
    '#.#L#L#.##'
]
sample_layout_5 = [
    '#.#L.L#.##',
    '#LLL#LL.L#',
    'L.#.L..#..',
    '#L##.##.L#',
    '#.#L.LL.LL',
    '#.#L#L#.##',
    '..L.L.....',
    '#L#L##L#L#',
    '#.LLLLLL.L',
    '#.#L#L#.##'
]
sample_layout_last = sample_layout_5


@pytest.mark.parametrize('seat_row,expected', [
    ('L.LL', [
        {'filled': False, 'can_be_filled': True},
        {'filled': False, 'can_be_filled': False},
        {'filled': False, 'can_be_filled': True},
        {'filled': False, 'can_be_filled': True},
    ])
])
def test_get_seat_layout_row(seat_row: str, expected: List[day_11.Seat]):
    assert day_11.get_seat_layout_row(seat_row) == expected


@pytest.mark.parametrize('seat_layout_human,row,column,expected', [
    (sample_layout_2, 0, 0, 1),
    (sample_layout_2, 1, 1, 2),
    (sample_layout_2, 9, 9, 1),
    (sample_layout_2, 6, 9, 3),
])
def test_get_surrounding_seats_filled(seat_layout_human: List[str], row: int, column: int, expected: int):
    seat_layout = day_11.get_seat_layout(seat_layout_human)
    assert day_11.get_surrounding_seats_filled(seat_layout, row, column) == expected


@pytest.mark.parametrize('seat_layout,expected', [
    (sample_layout_0, sample_layout_1),
    (sample_layout_1, sample_layout_2),
    (sample_layout_2, sample_layout_3),
    (sample_layout_3, sample_layout_4),
    (sample_layout_4, sample_layout_5),
    (sample_layout_5, sample_layout_5)
])
def test_get_updated_seat_layout(seat_layout, expected):
    starting_layout = day_11.get_seat_layout(seat_layout)
    expected_layout = day_11.get_seat_layout(expected)
    assert day_11.get_updated_seat_layout(starting_layout) == expected_layout


@pytest.mark.parametrize('seat_layout,expected', [(sample_layout_0, sample_layout_last)])
def test_get_stable_seat_layout(seat_layout: List[str], expected: List[str]):
    starting_layout = day_11.get_seat_layout(seat_layout)
    expected_layout = day_11.get_seat_layout(expected)
    assert day_11.get_stable_seat_layout(starting_layout) == expected_layout


@pytest.mark.parametrize('seat_layout,expected', [(sample_layout_0, 37)])
def test_get_stable_seat_count(seat_layout: List[str], expected: int):
    starting_layout = day_11.get_seat_layout(seat_layout)
    stable_layout = day_11.get_stable_seat_layout(starting_layout)
    assert day_11.get_filled_seat_count(stable_layout) == expected


sample_layout_visible_1 = [
    '.......#.',
    '...#.....',
    '.#.......',
    '.........',
    '..#L....#',
    '....#....',
    '.........',
    '#........',
    '...#.....'
]
sample_layout_visible_2 = [
    '.............',
    '.L.L.#.#.#.#.',
    '.............'
]
sample_layout_visible_3 = [
    '.##.##.',
    '#.#.#.#',
    '##...##',
    '...L...',
    '##...##',
    '#.#.#.#',
    '.##.##.'
]


@pytest.mark.parametrize('seat_layout_human,row,column,expected', [
    (sample_layout_visible_1, 4, 3, 8),
    (sample_layout_visible_2, 1, 1, 0),
    (sample_layout_visible_3, 3, 3, 0)
])
def test_get_visible_seats_filled(seat_layout_human: List[str], row: int, column: int, expected: int):
    seat_layout = day_11.get_seat_layout(seat_layout_human)
    assert day_11.get_visible_seats_filled(seat_layout, row, column) == expected


@pytest.mark.parametrize('seat_layout,expected', [(sample_layout_0, 26)])
def test_get_stable_seat_count_visible_method(seat_layout: List[str], expected: int):
    starting_layout = day_11.get_seat_layout(seat_layout)
    stable_layout = day_11.get_stable_seat_layout_visible_method(starting_layout)
    assert day_11.get_filled_seat_count(stable_layout) == expected
