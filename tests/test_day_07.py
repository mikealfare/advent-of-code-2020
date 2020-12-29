from typing import Set

import pytest

from tests.conftest import day_07


@pytest.fixture
def sample_ruleset() -> day_07.RuleSet:
    return day_07.convert_human_rules_to_ruleset({
        'light red bags contain 1 bright white bag, 2 muted yellow bags.',
        'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
        'bright white bags contain 1 shiny gold bag.',
        'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
        'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
        'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
        'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
        'faded blue bags contain no other bags.',
        'dotted black bags contain no other bags.'
    })


@pytest.mark.parametrize('human_rule,expected_rule', [
    ('muted lavender bags contain 5 dull brown bags, 4 pale maroon bags, 2 drab orange bags.',
     {'muted lavender': {'dull brown': 5, 'pale maroon': 4, 'drab orange': 2}})
])
def test_convert_human_rule_to_rule(human_rule: str, expected_rule: day_07.RuleSet):
    assert day_07.convert_human_rule_to_rule(human_rule) == expected_rule


@pytest.mark.parametrize('bag,expected', [
    ('shiny gold', {'bright white', 'muted yellow', 'dark orange', 'light red'}),
    ('bright white', {'light red', 'dark orange'})
])
def test_get_bags_that_contain_given_bag(
        sample_ruleset: day_07.RuleSet,
        bag: day_07.Bag,
        expected: Set[day_07.Bag]
):
    assert day_07.get_bags_that_contain_given_bag(bag, sample_ruleset) == expected


@pytest.mark.parametrize('bag,expected', [('shiny gold', 32)])
def test_get_total_bags_within_given_bag(sample_ruleset: day_07.RuleSet, bag: day_07.Bag, expected: int):
    assert day_07.get_total_bags_within_given_bag(bag, sample_ruleset) == expected
