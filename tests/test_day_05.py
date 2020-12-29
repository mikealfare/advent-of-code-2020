import pytest

from tests.conftest import day_05


@pytest.mark.parametrize('binary_string,expected_seat_id', [
    ('BFFFBBFRRR', 567),
    ('FFFBBBFRRR', 119),
    ('BBFFBBFRLL', 820),
])
def test_get_seat_id(binary_string: str, expected_seat_id: int):
    assert day_05.get_seat_id(binary_string) == expected_seat_id
