from typing import List, Tuple

import pytest

from tests.conftest import day_13


@pytest.mark.parametrize('start_time,bus_ids,expected_bus_id,expected_wait', [
    (939, ['7', '13', '59', '31', '19'], 59, 5)
])
def test_get_departure_information(start_time: int, bus_ids: List[str], expected_bus_id: int, expected_wait: int):
    assert day_13.get_departure_information_for_next_departure(bus_ids, start_time) == (expected_wait, expected_bus_id)


@pytest.mark.parametrize('congruence_1,congruence_2,expected', [
    ((4, 5), (3, 4), (19, 20)),
    ((19, 20), (0, 3), (39, 60))
])
def test_solve_pairwise_congruence_system(
        congruence_1: Tuple[int, int],
        congruence_2: Tuple[int, int],
        expected: Tuple[int, int]
):
    assert day_13.solve_pairwise_congruence_system(congruence_1, congruence_2) == expected


@pytest.mark.parametrize('bus_ids,expected', [
    (['17', 'x', '13', '19'], 3417),
    (['67', '7', '59', '61'], 754018),
    (['67', 'x', '7', '59', '61'], 779210),
    (['67', '7', 'x', '59', '61'], 1261476),
    (['1789', '37', '47', '1889'], 1202161486),
    (['7', '13', 'x', 'x', '59', 'x', '31', '19'], 1068781)
])
def test_get_departure_time_for_first_sequential_departures(bus_ids: List[str], expected: int):
    assert day_13.get_departure_time_for_first_sequential_departures(bus_ids) == expected
