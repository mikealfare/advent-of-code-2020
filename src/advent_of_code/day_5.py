

class Seat:

    def __init__(self, binary_string: str):
        self.binary_string = binary_string

    @property
    def row(self) -> int:
        row_string = self.binary_string[:7]
        row_string = row_string.replace('F', '0').replace('B', '1')
        return int(row_string, 2)

    @property
    def column(self) -> int:
        column_string = self.binary_string[-3:]
        column_string = column_string.replace('L', '0').replace('R', '1')
        return int(column_string, 2)

    @property
    def id(self):
        return self.row * 8 + self.column


if __name__ == '__main__':
    with open('input_files/day_5.txt') as f:
        seat_binary_strings = [line.replace('\n', '') for line in f.readlines()]
    seats = [Seat(seat) for seat in seat_binary_strings]
    seat_ids = [seat.id for seat in seats]
    max_id = max(seat_ids)
    min_id = min(seat_ids)
    all_seats = set(range(min_id, max_id + 1))
    missing_seats = all_seats.difference(set(seat_ids))
    print(f'max seat id = {max_id}')
    print(f'missing seat ids = {missing_seats}')
