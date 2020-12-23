from typing import List, Set, Tuple, Union
from itertools import product


Point = Union[Tuple[int, ...]]


def parse_input(input_lines: List[str], dimensions: int = 3) -> Set[Point]:
    result = set()
    for y, line in enumerate(input_lines):
        for x, value in enumerate(line):
            if value == '#':
                point = [x, y]
                for dimension in range(2, dimensions):
                    point.append(0)
                result.add(tuple(point))
    return result


def get_adjacent_points(point: Point) -> Set[Point]:
    dimension = len(point)
    unit_cube_list = [[-1, 0, 1]] * dimension
    unit_cube: List[Point] = [p for p in product(*unit_cube_list)]
    adjacent_points = set()
    for relative_point in unit_cube:
        adjacent_point = tuple(x_0 + x for x_0, x in zip(point, relative_point))
        adjacent_points.add(adjacent_point)
    return adjacent_points


def get_all_adjacent_points(points: Set[Point]) -> Set[Point]:
    adjacent_points = set()
    for point in points:
        adjacent_points = adjacent_points.union(get_adjacent_points(point))
    return adjacent_points


def get_adjacent_active_points(point: Point, active_points: Set[Point]) -> Set[Point]:
    adjacent_points = get_adjacent_points(point)
    return adjacent_points.intersection(active_points)


def execute_cycle(active_points: Set[Point]) -> Set[Point]:
    adjacent_points = get_all_adjacent_points(active_points)
    new_active_points = set()
    for point in adjacent_points:
        if point in active_points:
            if len(get_adjacent_active_points(point, active_points)) in [3, 4]:  # point itself is not part of 2-3
                new_active_points.add(point)
        else:
            if len(get_adjacent_active_points(point, active_points)) == 3:
                new_active_points.add(point)
    return new_active_points


def execute_many_cycles(active_points: Set[Point], cycles: int) -> Set[Point]:
    for cycle in range(cycles):
        active_points = execute_cycle(active_points)
    return active_points


def main():
    input_lines = [
        '#.#.##.#',
        '#.####.#',
        '...##...',
        '#####.##',
        '#....###',
        '##..##..',
        '#..####.',
        '#...#.#.'
    ]
    initial_active_points = parse_input(input_lines)
    active_points = execute_many_cycles(initial_active_points, 6)
    print(f'after 6 cycles, there are {len(active_points)} active points')
    initial_active_hyper_points = parse_input(input_lines, 4)
    active_hyper_points = execute_many_cycles(initial_active_hyper_points, 6)
    print(f'after 6 cycles, there are {len(active_hyper_points)} active hyper points')


if __name__ == '__main__':
    main()
