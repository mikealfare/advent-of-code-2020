import pytest

from tests.conftest import day_11_classes as day_11


@pytest.fixture
def sample_layout_0():
    return day_11.SeatLayout([
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
    ])


@pytest.fixture
def sample_layout_1():
    return day_11.SeatLayout([
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
    ])


@pytest.fixture
def sample_layout_2():
    return day_11.SeatLayout([
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
    ])


@pytest.fixture
def sample_layout_3():
    return day_11.SeatLayout([
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
    ])


@pytest.fixture
def sample_layout_4():
    return day_11.SeatLayout([
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
    ])


@pytest.fixture
def sample_layout_5():
    return day_11.SeatLayout([
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
    ])


@pytest.mark.parametrize('seat,expected', [
    (day_11.Seat(0, 0), 1),
    (day_11.Seat(1, 1), 2),
    (day_11.Seat(9, 9), 1),
    (day_11.Seat(6, 9), 3),
])
def test_filled_seats_surrounding(sample_layout_2: day_11.SeatLayout, seat: day_11.Seat, expected: int):
    assert sample_layout_2.filled_seats_surrounding(seat) == expected


@pytest.mark.parametrize('seat_layout,expected', [
    (sample_layout_0, sample_layout_1),
    (sample_layout_1, sample_layout_2),
    (sample_layout_2, sample_layout_3),
    (sample_layout_3, sample_layout_4),
    (sample_layout_4, sample_layout_5),
    (sample_layout_5, sample_layout_5)
])
def test_update_seat_layout(seat_layout: day_11.SeatLayout, expected: day_11.SeatLayout):
    day_11.update_seat_layout(seat_layout)
    assert seat_layout == expected


def test_get_stable_seat_layout(sample_layout_0: day_11.SeatLayout, sample_layout_5: day_11.SeatLayout):
    day_11.get_stable_seat_layout(sample_layout_0)
    assert sample_layout_0 == sample_layout_5


def test_get_stable_seat_count(sample_layout_0: day_11.SeatLayout):
    day_11.get_stable_seat_layout(sample_layout_0)
    assert sample_layout_0.filled_seats == 37


@pytest.fixture
def sample_layout_visible_1():
    return day_11.SeatLayout([
        '.......#.',
        '...#.....',
        '.#.......',
        '.........',
        '..#L....#',
        '....#....',
        '.........',
        '#........',
        '...#.....'
    ])


@pytest.fixture
def sample_layout_visible_2():
    return day_11.SeatLayout([
        '.............',
        '.L.L.#.#.#.#.',
        '.............'
    ])


@pytest.fixture
def sample_layout_visible_3():
    return day_11.SeatLayout([
        '.##.##.',
        '#.#.#.#',
        '##...##',
        '...L...',
        '##...##',
        '#.#.#.#',
        '.##.##.'
    ])


@pytest.mark.parametrize('seat_layout,seat,expected', [
    (sample_layout_visible_1, day_11.Seat(4, 3), 8),
    (sample_layout_visible_2, day_11.Seat(1, 1), 0),
    (sample_layout_visible_3, day_11.Seat(3, 3), 0)
])
def test_get_visible_seats_filled(seat_layout: day_11.SeatLayout, seat: day_11.Seat, expected: int):
    assert seat_layout.filled_seats_visible_by(seat) == expected


def test_get_stable_seat_count_visible_method(sample_layout_0: day_11.SeatLayout):
    day_11.get_stable_seat_layout(sample_layout_0, visible_method=True)
    assert sample_layout_0.filled_seats == 26
