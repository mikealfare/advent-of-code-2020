from typing import List, Dict, Tuple, Set, Optional
from itertools import product
from copy import deepcopy
from pathlib import Path
from operator import add


Seat = Tuple[int, int]
SeatLayout = Dict[Seat, Dict[str, bool]]


def get_seat_layout(seat_rows: List[str]) -> SeatLayout:
    filled_map = {'#': True, 'L': False, '.': False}
    is_seat_map = {'#': True, 'L': True, '.': False}
    layout = {}
    for row, row_of_seats in enumerate(seat_rows):
        for column, single_seat in enumerate(row_of_seats):
            layout[(row, column)] = {'filled': filled_map[single_seat], 'is_seat': is_seat_map[single_seat]}
    return layout


def filled_seats(seat_layout: SeatLayout) -> Set[Seat]:
    return {seat for seat, attrs in seat_layout.items() if attrs['is_seat'] and attrs['filled']}


def empty_seats(seat_layout: SeatLayout) -> Set[Seat]:
    return {seat for seat, attrs in seat_layout.items() if attrs['is_seat'] and not attrs['filled']}


def is_seat(seat_layout: SeatLayout, seat: Seat) -> bool:
    if seat not in seat_layout:
        return False
    return seat_layout[seat]['is_seat']


def is_filled_seat(seat_layout: SeatLayout, seat: Seat) -> bool:
    if seat not in seat_layout:
        return False
    return seat_layout[seat]['filled']


def update_seat(seat_layout: SeatLayout, seat: Seat, is_filled: bool):
    if is_seat(seat_layout, seat):
        seat_layout[seat]['filled'] = is_filled


def get_next_seat(
        seat_layout: SeatLayout,
        seat: Seat,
        direction: Tuple[int, int],
        adjacent_only: bool
) -> Optional[Seat]:
    next_seat: Seat = tuple(map(add, seat, direction))
    if next_seat not in seat_layout:
        return None
    if adjacent_only or is_seat(seat_layout, next_seat):
        return next_seat
    return get_next_seat(seat_layout, next_seat, direction, adjacent_only)


def get_next_seats_filled(seat_layout: SeatLayout, seat: Seat, adjacent_only: bool) -> int:
    seat_count = 0
    eight_directions = set(product([-1, 0, 1], [-1, 0, 1])).difference({(0, 0)})
    for direction in eight_directions:
        next_seat = get_next_seat(seat_layout, seat, direction, adjacent_only)
        if is_filled_seat(seat_layout, next_seat):
            seat_count += 1
    return seat_count


def get_seats_to_fill(seat_layout: SeatLayout, adjacent_only: bool) -> Set[Seat]:
    seats = set()
    for seat in empty_seats(seat_layout):
        if get_next_seats_filled(seat_layout, seat, adjacent_only) == 0:
            seats.add(seat)
    return seats


def get_seats_to_empty(seat_layout: SeatLayout, adjacent_only: bool) -> Set[Seat]:
    seats = set()
    for seat in filled_seats(seat_layout):
        if adjacent_only and get_next_seats_filled(seat_layout, seat, adjacent_only) >= 4:
            seats.add(seat)
        elif not adjacent_only and get_next_seats_filled(seat_layout, seat, adjacent_only) >= 5:
            seats.add(seat)
    return seats


def get_stable_seat_layout(seat_layout: SeatLayout, adjacent_only: bool) -> SeatLayout:
    updated_seat_layout = deepcopy(seat_layout)
    seats_to_fill = get_seats_to_fill(updated_seat_layout, adjacent_only)
    seats_to_empty = get_seats_to_empty(updated_seat_layout, adjacent_only)
    while seats_to_fill or seats_to_empty:
        for seat in seats_to_fill:
            update_seat(updated_seat_layout, seat, True)
        for seat in seats_to_empty:
            update_seat(updated_seat_layout, seat, False)
        seats_to_fill = get_seats_to_fill(updated_seat_layout, adjacent_only)
        seats_to_empty = get_seats_to_empty(updated_seat_layout, adjacent_only)
    return updated_seat_layout


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_11.txt'):
    with open(file_path) as f:
        seat_rows = [line.strip() for line in f.readlines()]
    seat_layout = get_seat_layout(seat_rows)
    stable_seat_layout_adjacent = get_stable_seat_layout(seat_layout, True)
    print(f'there are {len(filled_seats(stable_seat_layout_adjacent))} filled seats in the stable adjacent layout')
    stable_seat_layout_visible = get_stable_seat_layout(seat_layout, False)
    print(f'there are {len(filled_seats(stable_seat_layout_visible))} filled seats in the stable visible layout')


if __name__ == '__main__':
    main()
