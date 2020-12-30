from dataclasses import dataclass
from typing import Union, List
from pathlib import Path
from math import cos, sin, radians


@dataclass
class Move:
    x: int
    y: int


@dataclass
class Turn:
    degrees: int


@dataclass
class Forward:
    distance: int


@dataclass
class Point:
    x: int = 0
    y: int = 0

    def move(self, move: Move):
        self.x += move.x
        self.y += move.y

    def rotate(self, turn: Turn):
        self.x, self.y = (
            self.x * int(cos(radians(turn.degrees))) - self.y * int(sin(radians(turn.degrees))),
            self.x * int(sin(radians(turn.degrees))) + self.y * int(cos(radians(turn.degrees)))
        )

    @property
    def manhattan_distance(self) -> int:
        return abs(self.x) + abs(self.y)


@dataclass
class Boat(Point):
    bearing: int = 0

    def turn(self, turn: Turn):
        self.bearing = (self.bearing + turn.degrees) % 360

    def move_forward(self, forward: Forward):
        self.move(Move(
            forward.distance * int(cos(radians(self.bearing))),
            forward.distance * int(sin(radians(self.bearing)))
        ))


Instruction = Union[Move, Turn, Forward]


def parse_instruction(human_instruction: str) -> Instruction:
    direction = human_instruction[0]
    amount = int(human_instruction[1:])
    if direction == 'N':
        return Move(0, amount)
    elif direction == 'E':
        return Move(amount, 0)
    elif direction == 'S':
        return Move(0, -amount)
    elif direction == 'W':
        return Move(-amount, 0)
    elif direction == 'L':
        return Turn(amount % 360)
    elif direction == 'R':
        return Turn(-amount % 360)
    elif direction == 'F':
        return Forward(amount)
    else:
        raise ValueError('ERROR - unsupported direction')


def parse_input(human_instructions: List[str]) -> List[Instruction]:
    return [parse_instruction(instruction) for instruction in human_instructions]


def execute_instruction_on_boat(boat: Boat, instruction: Instruction):
    if isinstance(instruction, Move):
        boat.move(instruction)
    elif isinstance(instruction, Turn):
        boat.turn(instruction)
    elif isinstance(instruction, Forward):
        boat.move_forward(instruction)


def execute_all_instructions_on_boat(boat: Boat, instructions: List[Instruction]):
    for instruction in instructions:
        execute_instruction_on_boat(boat, instruction)


def execute_instruction_on_waypoint(boat: Boat, waypoint: Point, instruction: Instruction):
    if isinstance(instruction, Move):
        waypoint.move(instruction)
    elif isinstance(instruction, Turn):
        waypoint.rotate(instruction)
    elif isinstance(instruction, Forward):
        boat.move(Move(waypoint.x * instruction.distance, waypoint.y * instruction.distance))


def execute_all_instructions_on_waypoint(boat: Boat, waypoint: Point, instructions: List[Instruction]):
    for instruction in instructions:
        execute_instruction_on_waypoint(boat, waypoint, instruction)


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_12.txt'):
    with open(file_path) as f:
        human_instructions = [line.strip() for line in f.readlines()]
    instructions = parse_input(human_instructions)
    boat = Boat()
    execute_all_instructions_on_boat(boat, instructions)
    print(f'the manhattan distance to the boat is {boat.manhattan_distance}')
    boat = Boat()
    waypoint = Point(10, 1)
    execute_all_instructions_on_waypoint(boat, waypoint, instructions)
    print(f'the manhattan distance to the boat is {boat.manhattan_distance}')


if __name__ == '__main__':
    main()
