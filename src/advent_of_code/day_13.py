from typing import List, Tuple, Dict


def get_departure_information_for_next_departure(start_time: int, bus_ids: List[int]) -> Tuple[int, int]:
    wait_times = [(bus_id, bus_id - (start_time % bus_id)) for bus_id in bus_ids]
    ordered_wait_times = sorted(wait_times, key=lambda x: x[1])
    next_bus_id, wait_time = ordered_wait_times[0]
    return next_bus_id, start_time + wait_time


def get_start_times(bus_ids: List[str]) -> List[Tuple[int, int]]:
    start_times = []
    for start_time, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            start_times.append((int(bus_id), start_time))
    return start_times


def is_sequential(start_times: Dict[int, int], first_bus_departure: int) -> bool:
    for bus_id, start_time in start_times.items():
        if bus_id % first_bus_departure != start_time:
            return False
    return True


def solve_congruence_system(a_1, n_1, a_2, n_2) -> int:
    for iteration in range(n_2):
        if (a_1 + n_1 * iteration) % n_2 == a_2:
            return a_1 + n_1 * iteration


def get_departure_time_for_first_sequential_departures(bus_ids: List[str]) -> int:
    """
    Implements sieve algorithm for solving the Chinese Remainder Theorem

    for bus_id in start_times:
        target = (bus_id__i - start_time__i) % bus_id__i
        x = a1 mod n1
    """
    start_times = get_start_times(bus_ids)
    congruence_system = [(-start_time % bus_id, bus_id) for bus_id, start_time in start_times]
    congruence_system.sort(key=lambda x: x[1], reverse=True)

    a, n = congruence_system[0]
    for a_i, n_i in congruence_system[1:]:
        a = solve_congruence_system(a_1=a, n_1=n, a_2=a_i, n_2=n_i)
        n = n * n_i
    return a


def main():
    with open('input_files/day_13.txt') as f:
        start_time = int(f.readline().strip())
        all_bus_ids = [bus_id for bus_id in f.readline().strip().split(',')]
        clean_bus_ids = [int(bus_id) for bus_id in all_bus_ids if bus_id != 'x']
        print(f'start time: {start_time}')
        print(f'bus_ids: {clean_bus_ids}')
        bus_id, departure_time = get_departure_information_for_next_departure(start_time, clean_bus_ids)
        answer = bus_id * (departure_time - start_time)
        print(f'the next bus to depart is {bus_id} at {departure_time}, with answer {answer}')
        first_sequential_start_time = get_departure_time_for_first_sequential_departures(all_bus_ids)
        print(f'the first sequential departures happen at {first_sequential_start_time}')


if __name__ == '__main__':
    main()
