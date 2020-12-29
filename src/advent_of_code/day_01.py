import math
from itertools import combinations
from pathlib import Path
from typing import Set


Expenses = Set[int]


def get_product_of_combinations_with_sum_limit(entries: Expenses, sum_limit: int, length: int = 2) -> int:
    return math.prod({combo for combo in combinations(entries, length) if sum(combo) == sum_limit}.pop())


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_01.txt'):
    with open(file_path) as f:
        expense_report_entries = {int(line.strip()) for line in f.readlines()}
    combo_2 = get_product_of_combinations_with_sum_limit(expense_report_entries, 2020)
    combo_3 = get_product_of_combinations_with_sum_limit(expense_report_entries, 2020, length=3)
    print(f'2 elements product = {combo_2}')
    print(f'3 elements product = {combo_3}')


if __name__ == '__main__':
    main()
