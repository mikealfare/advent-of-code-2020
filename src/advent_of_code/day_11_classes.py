from dataclasses import dataclass, astuple
from typing import List, Set, Optional
from itertools import product
from copy import deepcopy
from pathlib import Path


@dataclass
class Location:
    row: int
    column: int

    def is_adjacent_to(self, location: 'Location') -> bool:
        if all([
            location.row - self.row in [-1, 0, 1],
            location.column - self.column in [-1, 0, 1],
            location != self
        ]):
            return True
        return False

    def __eq__(self, other: 'Location'):
        return self.row == other.row and self.column == other.column

    def __hash__(self):
        return (self.row * 100) + self.column


@dataclass
class Seat(Location):
    filled: Optional[bool] = None

    def __hash__(self):
        return super().__hash__()


class SeatLayout:

    locations: Set[Location]

    def __init__(self, seat_layout: List[str]):
        self.locations = self.parse_layout(seat_layout)

    @staticmethod
    def parse_layout(seat_layout: List[str]) -> Set[Location]:
        locations = set()
        for row, seat_row in enumerate(seat_layout):
            for column, seat_position in enumerate(seat_row):
                if seat_position == '.':
                    locations.add(Location(row, column))
                elif seat_position in ['#', 'L']:
                    locations.add(Seat(row, column, (seat_position == '#')))
        return locations

    @property
    def seats(self) -> Set[Seat]:
        return {seat for seat in self.locations if isinstance(seat, Seat)}

    @property
    def filled_seats(self) -> int:
        return len({seat for seat in self.seats if seat.filled})

    def update_seats(self, updated_seats: Set[Seat]):
        self.locations = self.locations.difference(updated_seats)
        self.locations = self.locations.union(updated_seats)

    def filled_seats_surrounding(self, seat: Seat) -> int:
        return len({
            other_seat
            for other_seat in self.seats
            if other_seat.filled
            and other_seat.is_adjacent_to(seat)
        })

    def filled_seats_visible_by(self, seat: Seat) -> int:
        seat_count = 0
        for row, column in product([-1, 0, 1], [-1, 0, 1]):
            next_adjacent_location = Location(seat.row + row, seat.column + column)
            if next_adjacent_location != seat:
                next_visible_seat = self.get_next_visible_seat(seat, next_adjacent_location)
                if next_visible_seat and next_visible_seat.filled:
                    seat_count += 1
        return seat_count

    def get_next_visible_seat(self, seat: Seat, next_location: Location) -> Optional[Seat]:
        row, column = next_location.row - seat.row, next_location.column - seat.column
        while next_location not in self.seats:
            if next_location not in self.locations:
                return None
            next_location = Location(next_location.row + row, next_location.column + column)
        next_visible_seat = {seat for seat in self.seats if seat == next_location}.pop()
        return next_visible_seat

    def __eq__(self, other: 'SeatLayout'):
        this_seats = {astuple(seat) for seat in self.seats}
        other_seats = {astuple(seat) for seat in other.seats}
        return this_seats == other_seats


def update_seat_layout(seat_layout: SeatLayout):
    seats = deepcopy(seat_layout.seats)
    updated_seats = set()
    for seat in seats:
        surrounding_seats = seat_layout.filled_seats_surrounding(seat)
        if not seat.filled and surrounding_seats == 0:
            seat.filled = True
            updated_seats.add(seat)
        elif seat.filled and surrounding_seats >= 4:
            seat.filled = False
            updated_seats.add(seat)
    seat_layout.update_seats(updated_seats)


def update_seat_layout_visible_method(seat_layout: SeatLayout):
    seats = deepcopy(seat_layout.seats)
    updated_seats = set()
    for seat in seats:
        visible_seats = seat_layout.filled_seats_visible_by(seat)
        if not seat.filled and visible_seats == 0:
            seat.filled = True
            updated_seats.add(seat)
        if seat.filled and visible_seats >= 5:
            seat.filled = False
            updated_seats.add(seat)
    seat_layout.update_seats(updated_seats)


def get_stable_seat_layout(seat_layout: SeatLayout, visible_method: bool = False):
    while True:
        last_updated_seat_layout = deepcopy(seat_layout)
        if visible_method:
            update_seat_layout_visible_method(seat_layout)
        else:
            update_seat_layout(seat_layout)
        if seat_layout == last_updated_seat_layout:
            return


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_11.txt'):
    with open(file_path) as f:
        seat_rows = [line.strip() for line in f.readlines()]
    seat_layout = SeatLayout(seat_rows)
    get_stable_seat_layout(seat_layout)
    print(f'there are {seat_layout.filled_seats} filled seats in the stable layout')
    seat_layout = SeatLayout(seat_rows)
    get_stable_seat_layout(seat_layout, visible_method=True)
    print(f'there are {seat_layout.filled_seats} filled seats in the visible method stable layout')


if __name__ == '__main__':
    main()
