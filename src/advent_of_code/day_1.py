import math
from itertools import permutations


def get_permutations(entries: set, length: int) -> set:
    order_dependent = set(permutations(entries, length))
    order_independent = set()
    for perm in order_dependent:
        if perm == tuple(sorted(perm)):
            order_independent.add(perm)
    return order_independent


def get_permutations_with_sum_limit(entries: set, length: int, sum_limit: int) -> set:
    perms = get_permutations(entries, length)
    return {perm for perm in perms if sum(perm) == sum_limit}


if __name__ == '__main__':
    with open('input_files/day_1.txt') as f:
        expense_report_entries = {int(line.replace('\n', '')) for line in f.readlines()}
    print(expense_report_entries)
    target_combination_2 = get_permutations_with_sum_limit(
        entries=expense_report_entries,
        length=2,
        sum_limit=2020
    ).pop()
    target_combination_3 = get_permutations_with_sum_limit(
        entries=expense_report_entries,
        length=3,
        sum_limit=2020
    ).pop()
    print(f'2 elements = {target_combination_2}; product = {math.prod(target_combination_2)}')
    print(f'3 elements = {target_combination_3}; product = {math.prod(target_combination_3)}')
