import pytest

from tests.conftest import day_05


@pytest.mark.parametrize('binary_string,row,column,seat_id', [
    ('BFFFBBFRRR', 70, 7, 567),
    ('FFFBBBFRRR', 14, 7, 119),
    ('BBFFBBFRLL', 102, 4, 820),
])
def test_get_set_from_binary_string(binary_string: str, row: int, column: int, seat_id: int):
    seat = day_05.Seat(binary_string)
    assert seat.row == row
    assert seat.column == column
    assert seat.id == seat_id
