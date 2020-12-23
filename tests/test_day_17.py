from typing import List, Set, Tuple

import pytest

from tests.conftest import day_17


@pytest.mark.parametrize('input_lines,dimensions,expected', [
    ([
         '.#.',
         '..#',
         '###'
     ], 3, {(1, 0, 0), (2, 1, 0), (0, 2, 0), (1, 2, 0), (2, 2, 0)}),
    ([
         '.#.',
         '..#',
         '###'
     ], 4, {(1, 0, 0, 0), (2, 1, 0, 0), (0, 2, 0, 0), (1, 2, 0, 0), (2, 2, 0, 0)})
])
def test_parse_input(input_lines: List[str], dimensions: int, expected: Set[tuple]):
    assert day_17.parse_input(input_lines, dimensions) == expected


@pytest.mark.parametrize('point,expected_number', [
    ((0, 0, 0), 27),
    ((0, 0, 0, 0), 81)
])
def test_get_adjacent_points(point: day_17.Point, expected_number: int):
    assert len(day_17.get_adjacent_points(point)) == expected_number


@pytest.mark.parametrize('points,expected_number', [
    ({(0, 0, 0)}, 27),
    ({(0, 0, 0), (0, 1, 1)}, 42),
])
def test_get_all_adjacent_points(points: Set[day_17.Point], expected_number: int):
    assert len(day_17.get_all_adjacent_points(points)) == expected_number


@pytest.mark.parametrize('active_points,cycles,expected', [
    ({(1, 0, 0), (2, 1, 0), (0, 2, 0), (1, 2, 0), (2, 2, 0)}, 6, 112),
    ({(1, 0, 0, 0), (2, 1, 0, 0), (0, 2, 0, 0), (1, 2, 0, 0), (2, 2, 0, 0)}, 6, 848)
])
def test_execute_many_cycles(active_points: Set[day_17.Point], cycles: int, expected: int):
    assert len(day_17.execute_many_cycles(active_points, cycles)) == expected
