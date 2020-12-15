import math


def find_product_of_sum(inputs, sum_amount) -> int:
    inputs_inverted = set(sum_amount - entry for entry in inputs)
    targets = inputs & inputs_inverted
    return math.prod(targets)


if __name__ == '__main__':
    with open('exercise_1_input.csv') as f:
        expense_report_entries = set(int(line.replace('\n', '')) for line in f.readlines())
    print(find_product_of_sum(expense_report_entries, 2020))
