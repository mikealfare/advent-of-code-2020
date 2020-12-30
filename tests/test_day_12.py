from typing import Tuple

from tests.conftest import day_12

import pytest


@pytest.mark.parametrize('human_instruction,expected_x,expected_y,expected_bearing', [
    ('F10', 10, 0, 0),
    ('N3', 0, 3, 0),
    ('F7', 7, 0, 0),
    ('R90', 0, 0, 270),
    ('F11', 11, 0, 0)
])
def test_execute_instruction_on_boat(human_instruction: str, expected_x: int, expected_y: int, expected_bearing: int):
    instruction = day_12.parse_instruction(human_instruction)
    boat = day_12.Boat()
    day_12.execute_instruction_on_boat(boat, instruction)
    assert boat.x == expected_x
    assert boat.y == expected_y
    assert boat.bearing == expected_bearing


@pytest.mark.parametrize('human_instructions,expected', [
    (['F10', 'N3', 'F7', 'R90', 'F11'], 25)
])
def test_execute_all_instructions_on_boat(human_instructions, expected):
    instructions = day_12.parse_input(human_instructions)
    boat = day_12.Boat()
    day_12.execute_all_instructions_on_boat(boat, instructions)
    assert boat.manhattan_distance == expected


@pytest.mark.parametrize('human_instruction,boat_start,waypoint_start,expected_boat,expected_waypoint', [
    ('F10', (0, 0), (10, 1), (100, 10), (10, 1)),
    ('N3', (100, 10), (10, 1), (100, 10), (10, 4)),
    ('F7', (100, 10), (10, 4), (170, 38), (10, 4)),
    ('R90', (170, 38), (10, 4), (170, 38), (4, -10)),
    ('F11', (170, 38), (4, -10), (214, -72), (4, -10))
])
def test_execute_instruction_on_waypoint(
        human_instruction: str,
        boat_start: Tuple[int, int],
        waypoint_start: Tuple[int, int],
        expected_boat: Tuple[int, int],
        expected_waypoint: Tuple[int, int]
):
    instruction = day_12.parse_instruction(human_instruction)
    boat = day_12.Boat(*boat_start)
    waypoint = day_12.Point(*waypoint_start)
    day_12.execute_instruction_on_waypoint(boat, waypoint, instruction)
    assert (boat.x, boat.y) == expected_boat
    assert (waypoint.x, waypoint.y) == expected_waypoint


@pytest.mark.parametrize('human_instructions,expected', [
    (['F10', 'N3', 'F7', 'R90', 'F11'], 286)
])
def test_execute_all_instructions_on_waypoint(human_instructions, expected):
    instructions = day_12.parse_input(human_instructions)
    boat = day_12.Boat()
    waypoint = day_12.Point(10, 1)
    day_12.execute_all_instructions_on_waypoint(boat, waypoint, instructions)
    assert boat.manhattan_distance == expected
