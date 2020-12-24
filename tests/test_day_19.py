from typing import List

import pytest

from tests.conftest import day_19


sample_human_rules = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"'
]


@pytest.mark.parametrize('human_rule,expected', [
    (['0: 4 1 5'], {'000': '004 001 005'}),
    (['1: 2 3 | 3 2'], {'001': '002 003 | 003 002'}),
    (['2: 4 4 | 5 5'], {'002': '004 004 | 005 005'}),
    (['3: 4 5 | 5 4'], {'003': '004 005 | 005 004'}),
    (['4: "a"'], {'004': 'a'}),
    (['5: "b"'], {'005': 'b'}),
    (sample_human_rules, {
        '000': '004 001 005',
        '001': '002 003 | 003 002',
        '002': '004 004 | 005 005',
        '003': '004 005 | 005 004',
        '004': 'a',
        '005': 'b',
    })
])
def test_get_rules(human_rule: List[day_19.HumanRule], expected: day_19.Rule):
    assert day_19.get_rules(human_rule) == expected


@pytest.mark.parametrize('human_rules,expected', [
    (sample_human_rules, 'aaaabb | aaabab | abbabb | abbbab | aabaab | aabbbb | abaaab | ababbb')
])
def test_collapse_rules(human_rules: List[day_19.HumanRule], expected):
    rules = day_19.get_rules(human_rules)


@pytest.mark.parametrize('human_rules,message,expected', [
    (sample_human_rules, 'ababbb', True),
    (sample_human_rules, 'bababa', False),
    (sample_human_rules, 'abbbab', True),
    (sample_human_rules, 'aaabbb', False),
    (sample_human_rules, 'aaaabbb', False),
])
def test_is_valid_message(human_rules: List[day_19.HumanRule], message: day_19.Message, expected: bool):
    pass
