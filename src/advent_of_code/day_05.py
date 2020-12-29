from pathlib import Path


def get_seat_id(binary_string: str) -> int:
    return int(binary_string.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_05.txt'):
    with open(file_path) as f:
        seats = [line.strip() for line in f.readlines()]
    seat_ids = {get_seat_id(seat) for seat in seats}
    max_id = max(seat_ids)
    print(f'max seat id = {max_id}')
    min_id = min(seat_ids)
    all_seats = set(range(min_id, max_id + 1))
    missing_seats = all_seats.difference(seat_ids)
    print(f'missing seat ids = {missing_seats}')


if __name__ == '__main__':
    main()
