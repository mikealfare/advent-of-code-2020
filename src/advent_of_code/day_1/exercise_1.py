import math


def find_product_of_sum_pairs(inputs, sum_amount) -> int:
    inputs_inverted = set(sum_amount - entry for entry in inputs)
    targets = inputs & inputs_inverted
    return math.prod(targets)


def add_dimension(sum_map, entries) -> dict:
    new_sum_map = dict()
    for entry in entries:
        for sum_of_values, values in sum_map.items():
            if not values or entry not in values:
                new_sum_map.update({sum_of_values + entry: values.append(entry)})
    return new_sum_map


def find_product_of_sum_n(inputs, sum_amount, number_of_entries) -> int:
    sum_map = {0: []}
    for n in range(number_of_entries):
        sum_map = add_dimension(sum_map, inputs)
    targets = sum_map[sum_amount]
    return targets
    # return math.prod(targets)


if __name__ == '__main__':
    with open('exercise_1_input.csv') as f:
        expense_report_entries = set(int(line.replace('\n', '')) for line in f.readlines())
    print(find_product_of_sum_n(expense_report_entries, 2020, 3))
