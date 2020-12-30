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


@pytest.mark.parametrize('seat_layout,expected', [
    (['L.L', '.L#'],
     {
         (0, 0): {'filled': False, 'is_seat': True},
         (0, 1): {'filled': False, 'is_seat': False},
         (0, 2): {'filled': False, 'is_seat': True},
         (1, 0): {'filled': False, 'is_seat': False},
         (1, 1): {'filled': False, 'is_seat': True},
         (1, 2): {'filled': True, 'is_seat': True},
     })
])
def test_get_seat_layout(seat_layout: List[str], expected: day_11.SeatLayout):
    assert day_11.get_seat_layout(seat_layout) == expected


@pytest.mark.parametrize('seat_layout_human,seat,adjacent_only,expected', [
    (sample_layout_2, (0, 0), True, 1),
    (sample_layout_2, (1, 1), True, 2),
    (sample_layout_2, (9, 9), True, 1),
    (sample_layout_2, (6, 9), True, 3),
    (sample_layout_visible_1, (4, 3), False, 8),
    (sample_layout_visible_2, (1, 1), False, 0),
    (sample_layout_visible_3, (3, 3), False, 0)
])
def test_get_surrounding_seats_filled(
        seat_layout_human: List[str],
        seat: day_11.Seat,
        adjacent_only: bool,
        expected: int
):
    seat_layout = day_11.get_seat_layout(seat_layout_human)
    assert day_11.get_next_seats_filled(seat_layout, seat, adjacent_only) == expected


@pytest.mark.parametrize('seat_layout,adjacent_only,expected', [
    (sample_layout_0, True, sample_layout_5)
])
def test_get_stable_seat_layout(seat_layout: List[str], adjacent_only: bool, expected: List[str]):
    starting_layout = day_11.get_seat_layout(seat_layout)
    expected_layout = day_11.get_seat_layout(expected)
    assert day_11.get_stable_seat_layout(starting_layout, adjacent_only) == expected_layout


@pytest.mark.parametrize('seat_layout,adjacent_only,expected', [
    (sample_layout_0, True, 37),
    (sample_layout_0, False, 26)
])
def test_get_stable_seat_count(seat_layout: List[str], adjacent_only: bool, expected: int):
    starting_layout = day_11.get_seat_layout(seat_layout)
    stable_layout = day_11.get_stable_seat_layout(starting_layout, adjacent_only)
    assert len(day_11.filled_seats(stable_layout)) == expected
