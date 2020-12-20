import pytest
from tests.conftest import day_07


@pytest.mark.parametrize('rule,color', [
    ('muted lavender bags contain 5 dull brown bags, 4 pale maroon bags, 2 drab orange bags.', 'muted lavender')
])
def test_parse_bag_color_from_rule(rule, color):
    rule = day_07.convert_human_rule_to_dict(rule)
    assert color in rule


@pytest.mark.parametrize('rule,color,contained_bags', [
    ('muted lavender bags contain 5 dull brown bags, 4 pale maroon bags, 2 drab orange bags.',
     'muted lavender',
     {'dull brown': 5, 'pale maroon': 4, 'drab orange': 2})
])
def test_parse_contained_bags_from_rule(rule, color, contained_bags):
    rule = day_07.convert_human_rule_to_dict(rule)
    assert rule[color] == contained_bags


sample_rules = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'
]


@pytest.mark.parametrize('bags,expected', [
    ({'shiny gold'}, {'bright white', 'muted yellow'}),
    ({'shiny gold', 'bright white'}, {'bright white', 'muted yellow', 'light red', 'dark orange'}),
])
def test_get_bags_that_contain_given_bags_directly(bags: set, expected: set):
    ruleset = day_07.convert_human_rules_to_ruleset_dict(sample_rules)
    assert day_07.get_bags_that_contain_given_bags_directly(bags=bags, ruleset=ruleset) == expected


def test_get_bags_that_contain_given_bag():
    ruleset = day_07.convert_human_rules_to_ruleset_dict(sample_rules)
    expected = {'bright white', 'muted yellow', 'dark orange', 'light red'}
    assert day_07.get_bags_that_contain_given_bag('shiny gold', ruleset) == expected


def test_get_total_bags_within_given_bag():
    ruleset = day_07.convert_human_rules_to_ruleset_dict(sample_rules)
    assert day_07.get_total_bags_within_given_bag('shiny gold', ruleset) == 32
