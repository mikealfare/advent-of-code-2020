from typing import Set

import pytest

from tests.conftest import day_16


@pytest.mark.parametrize('human_rule,field,valid_values', [
    ('class: 1-3 or 5-7', 'class', [(1, 3), (5, 7)]),
    ('row: 6-11 or 33-44', 'row', [(6, 11), (33, 44)]),
    ('seat: 13-40 or 45-50', 'seat', [(13, 40), (45, 50)])
])
def test_parse_human_rule(human_rule: str, field: str, valid_values: day_16.ValidValues):
    assert day_16.parse_human_rule(human_rule) == (field, valid_values)


def test_parse_input():
    rules, your_ticket, nearby_tickets = day_16.parse_input()
    assert len(rules) == 20
    assert your_ticket == (61, 151, 137, 191, 59, 163, 89, 83, 71, 179, 67, 149, 197, 167, 181, 173, 53, 139, 193, 157)
    assert len(nearby_tickets) == 241


sample_rules_1 = {
    'class': [(1, 3), (5, 7)],
    'row': [(6, 11), (33, 44)],
    'seat': [(13, 40), (45, 50)]
}


@pytest.mark.parametrize('ticket,rules,expected', [
    ((7, 3, 47), sample_rules_1, 0),
    ((40, 4, 50), sample_rules_1, 4),
    ((55, 2, 20), sample_rules_1, 55),
    ((38, 6, 12), sample_rules_1, 12)
])
def test_get_sum_of_invalid_values(ticket: day_16.Ticket, rules: day_16.Rules, expected: int):
    assert day_16.get_sum_of_invalid_values(ticket, rules) == expected


sample_rules_2 = {
    'class': [(0, 1), (4, 19)],
    'row': [(0, 5),  (8, 19)],
    'seat': [(0, 13), (16, 19)]
}
sample_tickets = {
    (11, 12, 13),
    (3, 9, 18),
    (15, 1, 5),
    (5, 14, 9)
}


@pytest.mark.parametrize('field_values,valid_ranges,expected', [
    ({ticket[0] for ticket in sample_tickets}, sample_rules_2['class'], False),
    ({ticket[1] for ticket in sample_tickets}, sample_rules_2['class'], True),
    ({ticket[2] for ticket in sample_tickets}, sample_rules_2['class'], True),
    ({ticket[0] for ticket in sample_tickets}, sample_rules_2['row'], True),
    ({ticket[1] for ticket in sample_tickets}, sample_rules_2['row'], True),
    ({ticket[2] for ticket in sample_tickets}, sample_rules_2['row'], True),
    ({ticket[0] for ticket in sample_tickets}, sample_rules_2['seat'], False),
    ({ticket[1] for ticket in sample_tickets}, sample_rules_2['seat'], False),
    ({ticket[2] for ticket in sample_tickets}, sample_rules_2['seat'], True),
])
def test_is_valid_field(field_values: Set[int], valid_ranges: day_16.ValidValues, expected: bool):
    assert day_16.is_valid_field(field_values, valid_ranges) == expected


@pytest.mark.parametrize('rules,tickets,expected', [
    (sample_rules_2, sample_tickets, {'class': {1, 2}, 'row': {0, 1, 2}, 'seat': {2}})
])
def test_get_valid_positions_for_all_fields(rules: day_16.Rules, tickets: Set[day_16.Ticket], expected: Set[int]):
    assert day_16.get_valid_positions_for_all_fields(rules, tickets) == expected


@pytest.mark.parametrize('rules,tickets,expected', [
    (sample_rules_2, sample_tickets, {'class': 1, 'row': 0, 'seat': 2})
])
def test_get_field_assignment(rules, tickets, expected):
    assert day_16.get_field_assignment(rules, tickets) == expected
