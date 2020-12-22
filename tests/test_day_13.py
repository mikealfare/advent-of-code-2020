import pytest

from tests.conftest import day_13


@pytest.mark.parametrize('start_time,bus_ids,expected_bus_id,expected_departure', [
    (939, [7, 13, 59, 31, 19], 59, 944)
])
def test_get_departure_information(start_time, bus_ids, expected_bus_id, expected_departure):
    bus_id, departure_time = day_13.get_departure_information_for_next_departure(start_time, bus_ids)
    assert bus_id == expected_bus_id
    assert departure_time == expected_departure


@pytest.mark.parametrize('bus_ids,expected', [
    (['17', 'x', '13', '19'], [(17, 0), (13, 2), (19, 3)]),
    (['67', '7', '59', '61'], [(67, 0), (7, 1), (59, 2), (61, 3)]),
    (['67', 'x', '7', '59', '61'], [(67, 0), (7, 2), (59, 3), (61, 4)]),
    (['67', '7', 'x', '59', '61'], [(67, 0), (7, 1), (59, 3), (61, 4)]),
    (['1789', '37', '47', '1889'], [(1789, 0), (37, 1), (47, 2), (1889, 3)]),
    (['7', '13', 'x', 'x', '59', 'x', '31', '19'], [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)])
])
def test_get_start_times(bus_ids, expected):
    assert day_13.get_start_times(bus_ids) == expected


@pytest.mark.parametrize('bus_ids,expected', [
    (['17', 'x', '13', '19'], 3417),
    (['67', '7', '59', '61'], 754018),
    (['67', 'x', '7', '59', '61'], 779210),
    (['67', '7', 'x', '59', '61'], 1261476),
    (['1789', '37', '47', '1889'], 1202161486),
    (['7', '13', 'x', 'x', '59', 'x', '31', '19'], 1068781)
])
def test_get_departure_time_for_first_sequential_departures(bus_ids, expected):
    assert day_13.get_departure_time_for_first_sequential_departures(bus_ids) == expected


@pytest.mark.parametrize('a_1,n_1,a_2,n_2,expected', [
    (4, 5, 3, 4, 19),
    (19, 20, 0, 3, 39)
])
def test_solve_congruence_system(a_1, n_1, a_2, n_2, expected):
    assert day_13.solve_congruence_system(a_1, n_1, a_2, n_2) == expected
