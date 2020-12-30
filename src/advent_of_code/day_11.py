from typing import List, Dict
from itertools import product
from copy import deepcopy
from pathlib import Path


Seat = Dict[str, bool]
SeatLayout = List[List[Seat]]


filled_map = {'#': True, 'L': False, '.': False}
can_be_filled_map = {'#': True, 'L': True, '.': False}


def get_seat_layout_row(seat_row: str) -> List[Seat]:
    row = []
    for each_seat in seat_row:
        seat = {
            'filled': filled_map[each_seat],
            'can_be_filled': can_be_filled_map[each_seat]
        }
        row.append(seat)
    return row


def get_seat_layout(seat_rows: List[str]) -> SeatLayout:
    layout = []
    for each_row in seat_rows:
        layout.append(get_seat_layout_row(each_row))
    return layout


def get_surrounding_seats_filled(seat_layout: SeatLayout, row: int, column: int) -> int:
    seats_to_check = [
        (row + row_offset, column + column_offset)
        for row_offset, column_offset in product([-1, 0, 1], [-1, 0, 1])
        if (
            (row_offset != 0 or column_offset != 0) and
            row + row_offset in range(len(seat_layout)) and
            column + column_offset in range(len(seat_layout[0]))
        )
    ]
    is_seat_filled = [
        seat_layout[check_row][check_column]['filled']
        for check_row, check_column in seats_to_check
    ]
    return len([seat for seat in is_seat_filled if seat])


def is_next_visible_seat_filled(
        seat_layout: SeatLayout,
        row: int,
        column: int,
        row_direction: int,
        column_direction: int
) -> bool:
    next_row = row + row_direction
    next_column = column + column_direction
    if next_row not in range(len(seat_layout)) or next_column not in range(len(seat_layout[0])):
        return False
    next_seat = seat_layout[next_row][next_column]
    if next_seat['can_be_filled']:
        return next_seat['filled']
    return is_next_visible_seat_filled(seat_layout, next_row, next_column, row_direction, column_direction)


def get_visible_seats_filled(seat_layout: SeatLayout, row: int, column: int) -> int:
    seat_count = 0
    for row_offset, column_offset in product([-1, 0, 1], [-1, 0, 1]):
        if row_offset != 0 or column_offset != 0:
            if is_next_visible_seat_filled(seat_layout, row, column, row_offset, column_offset):
                seat_count += 1
    return seat_count


def get_updated_seat_layout(seat_layout: SeatLayout) -> SeatLayout:
    updated_seat_layout = deepcopy(seat_layout)
    for row, column in product(range(len(seat_layout)), range(len(seat_layout[0]))):
        if not seat_layout[row][column]['can_be_filled']:
            continue
        if not seat_layout[row][column]['filled'] and get_surrounding_seats_filled(seat_layout, row, column) == 0:
            updated_seat_layout[row][column]['filled'] = True
        if seat_layout[row][column]['filled'] and get_surrounding_seats_filled(seat_layout, row, column) >= 4:
            updated_seat_layout[row][column]['filled'] = False
    return updated_seat_layout


def get_stable_seat_layout(seat_layout: SeatLayout) -> SeatLayout:
    updated_seat_layout = deepcopy(seat_layout)
    while True:
        last_updated_seat_layout = deepcopy(updated_seat_layout)
        updated_seat_layout = get_updated_seat_layout(updated_seat_layout)
        if updated_seat_layout == last_updated_seat_layout:
            return updated_seat_layout


def get_updated_seat_layout_visible_method(seat_layout: SeatLayout) -> SeatLayout:
    updated_seat_layout = deepcopy(seat_layout)
    for row, column in product(range(len(seat_layout)), range(len(seat_layout[0]))):
        if not seat_layout[row][column]['can_be_filled']:
            continue
        if not seat_layout[row][column]['filled'] and get_visible_seats_filled(seat_layout, row, column) == 0:
            updated_seat_layout[row][column]['filled'] = True
        if seat_layout[row][column]['filled'] and get_visible_seats_filled(seat_layout, row, column) >= 5:
            updated_seat_layout[row][column]['filled'] = False
    return updated_seat_layout


def get_stable_seat_layout_visible_method(seat_layout: SeatLayout) -> SeatLayout:
    updated_seat_layout = deepcopy(seat_layout)
    while True:
        last_updated_seat_layout = deepcopy(updated_seat_layout)
        updated_seat_layout = get_updated_seat_layout_visible_method(updated_seat_layout)
        if updated_seat_layout == last_updated_seat_layout:
            return updated_seat_layout


def get_filled_seat_count(seat_layout: SeatLayout) -> int:
    filled_count = 0
    for row, column in product(range(len(seat_layout)), range(len(seat_layout[0]))):
        if seat_layout[row][column]['filled']:
            filled_count += 1
    return filled_count


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_11.txt'):
    with open(file_path) as f:
        seat_rows = [line.strip() for line in f.readlines()]
    seat_layout = get_seat_layout(seat_rows)
    stable_seat_layout = get_stable_seat_layout(seat_layout)
    stable_seat_count = get_filled_seat_count(stable_seat_layout)
    print(f'there are {stable_seat_count} filled seats in the stable layout')
    stable_seat_layout_visible_method = get_stable_seat_layout_visible_method(seat_layout)
    stable_seat_count_visible_method = get_filled_seat_count(stable_seat_layout_visible_method)
    print(f'there are {stable_seat_count_visible_method} filled seats in the visible method stable layout')


if __name__ == '__main__':
    main()
