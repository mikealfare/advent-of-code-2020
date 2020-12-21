from dataclasses import dataclass
from typing import Union, List


@dataclass
class Point:
    x: int = 0
    y: int = 0

    @property
    def manhattan_distance(self) -> int:
        return abs(self.x) + abs(self.y)


@dataclass
class Waypoint(Point):
    pass


@dataclass
class Boat(Point):
    bearing: str = 'E'


@dataclass
class Move:
    direction: str
    distance: int


@dataclass
class Turn:
    direction: str
    degrees: int


def get_instruction_from_input(human_instruction: str) -> Union[Turn, Move]:
    direction = human_instruction[0]
    amount = int(human_instruction[1:])
    if direction in 'NSEWF':
        return Move(direction=direction, distance=amount)
    elif direction in 'LR':
        return Turn(direction=direction, degrees=amount)
    else:
        raise ValueError('ERROR - unsupported direction')


def get_instructions_from_input(human_instructions: List[str]) -> List[Union[Turn, Move]]:
    instructions = []
    for instruction in human_instructions:
        instructions.append(get_instruction_from_input(instruction))
    return instructions


def move_point(point: 'Point', move: 'Move'):
    if isinstance(point, Boat) and move.direction == 'F':
        direction = point.bearing
    else:
        direction = move.direction

    if direction == 'N':
        point.y = point.y + move.distance
    elif direction == 'E':
        point.x = point.x + move.distance
    elif direction == 'S':
        point.y = point.y - move.distance
    elif direction == 'W':
        point.x = point.x - move.distance
    else:
        raise ValueError('ERROR - unexpected direction')


def turn_boat(boat: 'Boat', turn: 'Turn'):
    bearing_map = {'N': 0, 'E': 90, 'S': 180, 'W': 270}
    bearing_map_inverse = {degrees: bearing for bearing, degrees in bearing_map.items()}
    direction_map = {'R': 1, 'L': -1}

    boat_bearing_degrees = bearing_map[boat.bearing]
    degrees = direction_map[turn.direction] * turn.degrees
    new_boat_bearing_degrees = (boat_bearing_degrees + degrees) % 360
    boat.bearing = bearing_map_inverse[new_boat_bearing_degrees]


def execute_instruction_on_boat(boat: 'Boat', instruction: 'Union[Turn, Move]'):
    if isinstance(instruction, Turn):
        turn_boat(boat, instruction)
    elif isinstance(instruction, Move):
        move_point(boat, instruction)
    else:
        raise ValueError('ERROR - unsupported action')


def execute_all_instructions_on_boat(boat: 'Boat', instructions: List[Union[Turn, Move]]):
    for instruction in instructions:
        execute_instruction_on_boat(boat, instruction)


def move_boat_towards_waypoint(boat: 'Boat', waypoint: 'Waypoint', move: 'Move'):
    move_x = Move(direction='E', distance=(waypoint.x - boat.x) * move.distance)
    move_y = Move(direction='N', distance=(waypoint.y - boat.y) * move.distance)
    move_point(boat, move_x)
    move_point(boat, move_y)
    move_point(waypoint, move_x)
    move_point(waypoint, move_y)


def turn_waypoint_around_boat(boat: 'Boat', waypoint: 'Waypoint', turn: 'Turn'):
    diff_x = waypoint.x - boat.x
    diff_y = waypoint.y - boat.y
    if turn.degrees == 180:
        move_point(waypoint, Move(direction='W', distance=2 * diff_x))
        move_point(waypoint, Move(direction='S', distance=2 * diff_y))
    elif (turn.degrees == 90 and turn.direction == 'R') or (turn.degrees == 270 and turn.direction == 'L'):
        move_point(waypoint, Move(direction='W', distance=diff_x - diff_y))
        move_point(waypoint, Move(direction='S', distance=diff_x + diff_y))
    elif (turn.degrees == 90 and turn.direction == 'L') or (turn.degrees == 270 and turn.direction == 'R'):
        move_point(waypoint, Move(direction='W', distance=diff_x + diff_y))
        move_point(waypoint, Move(direction='N', distance=diff_x - diff_y))
    else:
        raise ValueError('ERROR - unsupported waypoint turn')


def execute_instruction_on_waypoint(boat: 'Boat', waypoint: 'Waypoint', instruction: 'Union[Turn, Move]'):
    if isinstance(instruction, Move) and instruction.direction == 'F':
        move_boat_towards_waypoint(boat, waypoint, instruction)
    elif isinstance(instruction, Move) and instruction.direction in 'NSEW':
        move_point(waypoint, instruction)
    elif isinstance(instruction, Turn):
        turn_waypoint_around_boat(boat, waypoint, instruction)
    else:
        raise ValueError('ERROR - unsupported instruction')


def execute_all_instructions_on_waypoint(boat: 'Boat', waypoint: 'Waypoint', instructions: 'List[Union[Turn, Move]]'):
    for instruction in instructions:
        execute_instruction_on_waypoint(boat, waypoint, instruction)


def main():
    with open('input_files/day_12.txt') as f:
        human_instructions = [line.strip().replace('\n', '') for line in f.readlines()]
    instructions = get_instructions_from_input(human_instructions)
    boat = Boat()
    execute_all_instructions_on_boat(boat, instructions)
    print(f'the manhattan distance to the boat is {boat.manhattan_distance}')
    boat = Boat()
    waypoint = Waypoint(x=10, y=1)
    execute_all_instructions_on_waypoint(boat, waypoint, instructions)
    print(f'the manhattan distance to the boat is {boat.manhattan_distance}')


if __name__ == '__main__':
    main()
