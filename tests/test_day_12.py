from tests.conftest import day_12

import pytest

sample_instructions = ['F10', 'N3', 'F7', 'R90', 'F11']


@pytest.mark.parametrize('human_instruction,expected_x,expected_y,expected_bearing', [
    ('F10', 10, 0, 'E'),
    ('N3', 0, 3, 'E'),
    ('F7', 7, 0, 'E'),
    ('R90', 0, 0, 'S'),
    ('F11', 11, 0, 'E')
])
def test_execute_instruction_on_boat(human_instruction: str, expected_x: int, expected_y: int, expected_bearing: str):
    instruction = day_12.get_instruction_from_input(human_instruction)
    boat = day_12.Boat()
    day_12.execute_instruction_on_boat(boat, instruction)
    assert boat.x == expected_x
    assert boat.y == expected_y
    assert boat.bearing == expected_bearing


@pytest.mark.parametrize('human_instructions,expected', [(sample_instructions, 25)])
def test_execute_all_instructions_on_boat(human_instructions, expected):
    instructions = day_12.get_instructions_from_input(human_instructions)
    boat = day_12.Boat()
    day_12.execute_all_instructions_on_boat(boat, instructions)
    assert boat.manhattan_distance == expected


@pytest.mark.parametrize('human_instructions,expected', [(sample_instructions, 286)])
def test_execute_all_instructions_on_waypoint(human_instructions, expected):
    instructions = day_12.get_instructions_from_input(human_instructions)
    boat = day_12.Boat()
    waypoint = day_12.Waypoint(x=10, y=1)
    day_12.execute_all_instructions_on_waypoint(boat, waypoint, instructions)
    assert boat.manhattan_distance == expected
