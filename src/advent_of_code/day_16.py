from typing import Dict, List, Tuple, Set
from pathlib import Path
from math import prod


def parse_human_rule(human_rule: str) -> Dict[str, List[Tuple[int, int]]]:
    """
    e.g.: departure_location: [(a, b), (c, d)]
    """
    field_name, valid_ranges = human_rule.split(':')
    field_name.replace(' ', '_')
    valid_ranges_strings = [tuple(valid_range.split('-')) for valid_range in valid_ranges.split('or')]
    valid_ranges = []
    for start, end in valid_ranges_strings:
        valid_range = int(start.strip()), int(end.strip())
        valid_ranges.append(valid_range)
    return {field_name: valid_ranges}


def parse_input() -> Tuple[Dict[str, List[Tuple[int, int]]], List[int], List[List[int]]]:
    with open(Path(__file__).parent / 'input_files' / 'day_16.txt') as f:
        rules = {}
        for i in range(20):
            rules.update(parse_human_rule(f.readline().strip()))
        for i in range(2):
            skipped_lines = f.readline()
        your_ticket = [int(number) for number in f.readline().strip().split(',')]
        for i in range(2):
            skipped_lines = f.readline()
        nearby_tickets = []
        for i in range(241):
            nearby_tickets.append([int(number) for number in f.readline().strip().split(',')])
        return rules, your_ticket, nearby_tickets


def is_valid_value(value: int, rule_ranges: List[Tuple[int, int]]) -> bool:
    for rule_range in rule_ranges:
        if value in range(rule_range[0], rule_range[1] + 1):
            return True
    return False


def get_globally_invalid_values_on_ticket(ticket: List[int], rules: Dict[str, List[Tuple[int, int]]]) -> Set[int]:
    invalid_values = set()
    for value in ticket:
        is_invalid = True
        for rule_ranges in rules.values():
            if is_valid_value(value, rule_ranges):
                is_invalid = False
        if is_invalid:
            invalid_values.add(value)
    return invalid_values


def is_valid_field(rule_ranges: List[Tuple[int, int]], field_values: List[int]) -> bool:
    for value in field_values:
        if not is_valid_value(value, rule_ranges):
            return False
    return True


def get_valid_fields_by_rule(rules: Dict[str, List[Tuple[int, int]]], tickets: List[List[int]]) -> Dict[str, List[int]]:
    field_values = {}
    for i in range(len(tickets[0])):
        field_values.update({i: [ticket[i] for ticket in tickets]})

    valid_fields = {}
    for field_name, rule_ranges in rules.items():
        valid_fields.update({field_name: []})
        for field_position, values in field_values.items():
            if is_valid_field(rule_ranges, values):
                valid_fields[field_name].append(field_position)

    return valid_fields


def get_field_assignment(rules: Dict[str, List[Tuple[int, int]]], tickets: List[List[int]]) -> Dict[str, int]:
    valid_fields = get_valid_fields_by_rule(rules, tickets)
    field_assignment = {}

    while len(field_assignment) < len(valid_fields):
        for field_position in field_assignment.values():
            for valid_positions in valid_fields.values():
                if field_position in valid_positions:
                    valid_positions.remove(field_position)

        for field_name, valid_positions in valid_fields.items():
            if len(valid_positions) == 1:
                field_assignment.update({field_name: valid_positions[0]})

    return field_assignment


def get_ticket(ticket_values: List[int], field_assignment: Dict[str, int]) -> Dict[str, int]:
    return {field_name: ticket_values[field_position] for field_name, field_position in field_assignment.items()}


def main():
    rules, your_ticket, nearby_tickets = parse_input()
    invalid_values_sum = 0
    valid_tickets = []
    for ticket in nearby_tickets:
        invalid_values = get_globally_invalid_values_on_ticket(ticket, rules)
        if len(invalid_values) == 0:
            valid_tickets.append(ticket)
        invalid_values_sum += sum(invalid_values)
    print(f'the sum of all invalid values is: {invalid_values_sum}')
    valid_tickets.append(your_ticket)
    field_assignment = get_field_assignment(rules, valid_tickets)
    ticket = get_ticket(your_ticket, field_assignment)
    print(ticket)
    answer = prod([value for field, value in ticket.items() if 'departure' in field])
    print(f'the answer is {answer}')


if __name__ == '__main__':
    main()
