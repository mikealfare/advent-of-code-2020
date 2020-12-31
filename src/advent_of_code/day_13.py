from typing import List, Tuple
from functools import reduce


def get_departure_information_for_next_departure(bus_ids: List[str], start_time: int) -> Tuple[int, int]:
    wait_times = [
        (-start_time % int(bus_id), int(bus_id))
        for bus_id in bus_ids
        if bus_id != 'x'
    ]
    return sorted(wait_times, key=lambda x: x[0])[0]


def solve_pairwise_congruence_system(congruence_1: Tuple[int, int], congruence_2: Tuple[int, int]) -> Tuple[int, int]:
    a_1, n_1 = congruence_1
    a_2, n_2 = congruence_2
    for m in range(n_2):
        a = a_1 + n_1 * m
        if a % n_2 == a_2:
            return a, n_1 * n_2


def get_departure_time_for_first_sequential_departures(bus_ids: List[str]) -> int:
    """
    Implement sieve algorithm for solving the Chinese Remainder Theorem
    """
    congruence_system = [
        (-start_time % int(bus_id), int(bus_id))
        for start_time, bus_id in enumerate(bus_ids)
        if bus_id != 'x'
    ]
    congruence_system.sort(key=lambda x: x[1], reverse=True)
    departure_time, _ = reduce(solve_pairwise_congruence_system, congruence_system)
    return departure_time


def main():
    with open('input_files/day_13.txt') as f:
        start_time = int(f.readline().strip())
        bus_ids = [bus_id for bus_id in f.readline().strip().split(',')]
    wait_time, bus_id = get_departure_information_for_next_departure(bus_ids, start_time)
    print(f'the next bus to depart is {bus_id} in {wait_time}, with answer {bus_id * wait_time}')
    first_sequential_start_time = get_departure_time_for_first_sequential_departures(bus_ids)
    print(f'the first sequential departures start at {first_sequential_start_time}')


if __name__ == '__main__':
    main()
