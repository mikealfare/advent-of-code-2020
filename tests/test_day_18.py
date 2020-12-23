import pytest

from tests.conftest import day_18


@pytest.mark.parametrize('expression,expected', [
    ('1 + (2 * 3) + 4', ('1 +', '2 * 3', '+ 4')),
    ('(2 * 3) + 4', (None, '2 * 3', '+ 4')),
    ('1 + (2 * 3)', ('1 +', '2 * 3', None)),
    ('(2 * 3)', (None, '2 * 3', None))
])
def test_partition_first_contained_expression(expression, expected):
    assert day_18.partition_first_contained_expression(expression) == expected


@pytest.mark.parametrize('expression,expected', [
    ('1 + 2 * 3 + 4 * 5 + 6', '71'),
    ('1 + (2 * 3) + (4 * (5 + 6))', '51'),
    ('2 * 3 + (4 * 5)', '26'),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', '437'),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', '12240'),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', '13632'),
])
def test_evaluate_expression(expression: str, expected: str):
    assert day_18.evaluate_expression(expression) == expected


@pytest.mark.parametrize('expression,expected', [
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', '1445'),
    ('1 + 2 * 3 + 4 * 5 + 6', '231'),
    ('1 + (2 * 3) + (4 * (5 + 6))', '51'),
    ('2 * 3 + (4 * 5)', '46'),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', '669060'),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', '23340'),
])
def test_evaluate_expression_with_addition_first(expression: str, expected: str):
    assert day_18.evaluate_expression(expression, True) == expected
