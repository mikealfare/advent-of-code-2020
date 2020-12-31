import pytest
from tests.conftest import day_02


@pytest.mark.parametrize('rule,password,expected', [
    ('1-3 a', 'abcde', True),
    ('1-3 b', 'cdefg', False),
    ('2-9 c', 'ccccccccc', True),
])
def test_is_valid_by_count(rule: str, password: str, expected: bool):
    assert day_02.is_valid_by_count(rule, password) == expected


@pytest.mark.parametrize('rule,password,expected', [
    ('1-3 a', 'abcde', True),
    ('1-3 b', 'cdefg', False),
    ('2-9 c', 'ccccccccc', False),
    ('16-17 k', 'nphkpzqswcltkkbkk', False),
    ('8-11 l', 'qllllqllklhlvtl', True),
])
def test_is_valid_by_existence(rule: str, password: str, expected: bool):
    assert day_02.is_valid_by_existence(rule, password) == expected
