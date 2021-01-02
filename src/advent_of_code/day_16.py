from typing import Dict, List, Tuple, Set
from pathlib import Path
from math import prod


Ticket = Tuple[int, ...]
ValidValues = List[Tuple[int, int]]
Rules = Dict[str, ValidValues]


def parse_human_rule(human_rule: str) -> Tuple[str, ValidValues]:
    field_name, valid_values_string = human_rule.split(': ')
    field_name.replace(' ', '_')
    valid_values = [
        tuple(
            int(end_point)
            for end_point in valid_range.split('-')
        )
        for valid_range in valid_values_string.split(' or ')
    ]
    return field_name, valid_values


def parse_input() -> Tuple[Rules, Ticket, Set[Ticket]]:
    with open(Path(__file__).parent / 'input_files' / 'day_16.txt') as f:
        rules = {}
        for i in range(20):
            field, valid_values = parse_human_rule(f.readline().strip())
            rules[field] = valid_values
        for i in range(2):
            skipped_lines = f.readline()
        your_ticket = tuple(int(number) for number in f.readline().strip().split(','))
        for i in range(2):
            skipped_lines = f.readline()
        nearby_tickets = set()
        for i in range(241):
            nearby_tickets.add(tuple(int(number) for number in f.readline().strip().split(',')))
        return rules, your_ticket, nearby_tickets


def is_valid_value(value: int, valid_ranges: ValidValues) -> bool:
    return any({value in range(valid_range[0], valid_range[1] + 1) for valid_range in valid_ranges})


def get_sum_of_invalid_values(ticket: Ticket, rules: Rules) -> int:
    sum_of_invalid_values = 0
    for value in ticket:
        globally_invalid = all([
            not is_valid_value(value, valid_ranges)
            for valid_ranges in rules.values()
        ])
        if globally_invalid:
            sum_of_invalid_values += value
    return sum_of_invalid_values


def get_sum_of_invalid_values_by_ticket(tickets: Set[Ticket], rules: Rules) -> Dict[Ticket, int]:
    return {ticket: get_sum_of_invalid_values(ticket, rules) for ticket in tickets}


def get_all_values_by_field(tickets: Set[Ticket]) -> Dict[int, Set[int]]:
    field_values = {}
    for ticket in tickets:
        for field, value in enumerate(ticket):
            if field not in field_values:
                field_values[field] = set()
            field_values[field].add(value)
    return field_values


def is_valid_field(field_values: Set[int], valid_ranges: ValidValues) -> bool:
    return all({is_valid_value(value, valid_ranges) for value in field_values})


def get_valid_positions(valid_ranges: ValidValues, all_field_values: Dict[int, Set[int]]) -> Set[int]:
    return {
        field_position
        for field_position, field_values in all_field_values.items()
        if is_valid_field(field_values, valid_ranges)
    }


def get_valid_positions_for_all_fields(rules: Rules, tickets: Set[Ticket]) -> Dict[str, Set[int]]:
    all_field_values = get_all_values_by_field(tickets)
    valid_field_positions = {
        field_name: get_valid_positions(valid_ranges, all_field_values)
        for field_name, valid_ranges in rules.items()
    }
    return valid_field_positions


def get_field_assignment(rules: Rules, tickets: Set[Ticket]) -> Dict[str, int]:
    valid_field_positions = get_valid_positions_for_all_fields(rules, tickets)
    assigned_fields = {}

    while len(assigned_fields) < len(valid_field_positions):
        valid_field_positions.update({
            field_name: valid_positions.difference(assigned_fields.values())
            for field_name, valid_positions in valid_field_positions.items()
        })
        assigned_fields.update({
            field_name: valid_positions.pop()
            for field_name, valid_positions in valid_field_positions.items()
            if len(valid_positions) == 1
        })

    return assigned_fields


def get_ticket(ticket: Ticket, field_assignment: Dict[str, int]) -> Dict[str, int]:
    return {field_name: ticket[field_position] for field_name, field_position in field_assignment.items()}


def main():
    rules, your_ticket, nearby_tickets = parse_input()
    sum_of_invalid_values_by_ticket = get_sum_of_invalid_values_by_ticket(nearby_tickets, rules)
    sum_of_invalid_values = sum(sum_of_invalid_values_by_ticket.values())
    print(f'the sum of all invalid values is: {sum_of_invalid_values}')
    valid_tickets = {
        ticket
        for ticket, sum_of_invalid_values in sum_of_invalid_values_by_ticket.items()
        if sum_of_invalid_values == 0
    }
    valid_tickets.add(your_ticket)
    field_assignment = get_field_assignment(rules, valid_tickets)
    ticket = get_ticket(your_ticket, field_assignment)
    answer = prod([value for field, value in ticket.items() if 'departure' in field])
    print(f'the answer is {answer}')


if __name__ == '__main__':
    main()
