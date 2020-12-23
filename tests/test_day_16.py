import pytest

from tests.conftest import day_16


@pytest.mark.parametrize('human_rule,expected', [
    ('class: 1-3 or 5-7', {'class': [(1, 3), (5, 7)]}),
    ('row: 6-11 or 33-44', {'row': [(6, 11), (33, 44)]}),
    ('seat: 13-40 or 45-50', {'seat': [(13, 40), (45, 50)]})
])
def test_parse_human_rule(human_rule, expected):
    assert day_16.parse_human_rule(human_rule) == expected


def test_parse_input():
    rules, your_ticket, nearby_tickets = day_16.parse_input()
    assert len(rules) == 20
    assert your_ticket == [61, 151, 137, 191, 59, 163, 89, 83, 71, 179, 67, 149, 197, 167, 181, 173, 53, 139, 193, 157]
    assert len(nearby_tickets) == 241


sample_human_rules = [
    'class: 1-3 or 5-7',
    'row: 6-11 or 33-44',
    'seat: 13-40 or 45-50'
]


@pytest.mark.parametrize('ticket,human_rules,expected', [
    ([7, 3, 47], sample_human_rules, set()),
    ([40, 4, 50], sample_human_rules, {4}),
    ([55, 2, 20], sample_human_rules, {55}),
    ([38, 6, 12], sample_human_rules, {12})
])
def test_get_invalid_values_on_ticket(ticket, human_rules, expected):
    rules = {}
    for rule in human_rules:
        rules.update(day_16.parse_human_rule(rule))
    assert day_16.get_globally_invalid_values_on_ticket(ticket, rules) == expected


sample_rules = {
    'class': [(0, 1), (4, 19)],
    'row': [(0, 5),  (8, 19)],
    'seat': [(0, 13), (16, 19)]
}
sample_tickets = [
    [11, 12, 13],
    [3, 9, 18],
    [15, 1, 5],
    [5, 14, 9]
]


@pytest.mark.parametrize('rule_ranges,field_values,expected', [
    (sample_rules['class'], [ticket[0] for ticket in sample_tickets], False),
    (sample_rules['class'], [ticket[1] for ticket in sample_tickets], True),
    (sample_rules['class'], [ticket[2] for ticket in sample_tickets], True),
    (sample_rules['row'], [ticket[0] for ticket in sample_tickets], True),
    (sample_rules['row'], [ticket[1] for ticket in sample_tickets], True),
    (sample_rules['row'], [ticket[2] for ticket in sample_tickets], True),
    (sample_rules['seat'], [ticket[0] for ticket in sample_tickets], False),
    (sample_rules['seat'], [ticket[1] for ticket in sample_tickets], False),
    (sample_rules['seat'], [ticket[2] for ticket in sample_tickets], True),
])
def test_is_valid_field(rule_ranges, field_values, expected):
    assert day_16.is_valid_field(rule_ranges, field_values) == expected


@pytest.mark.parametrize('rules,tickets,expected', [
    (sample_rules, sample_tickets, {'class': [1, 2], 'row': [0, 1, 2], 'seat': [2]})
])
def test_get_valid_fields_by_rule(rules, tickets, expected):
    assert day_16.get_valid_fields_by_rule(rules, tickets) == expected


@pytest.mark.parametrize('rules,tickets,expected', [
    (sample_rules, sample_tickets, {'class': 1, 'row': 0, 'seat': 2})
])
def test_get_field_assignment(rules, tickets, expected):
    assert day_16.get_field_assignment(rules, tickets) == expected
