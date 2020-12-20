import pytest
from tests.conftest import day_02


@pytest.mark.parametrize(
    'rule_string,password,is_valid',
    [
        ('1-3 a', 'abcde', True),
        ('1-3 b', 'cdefg', False),
        ('2-9 c', 'ccccccccc', True),
    ]
)
def test_password_rule_count_validation(rule_string: str, password: str, is_valid: bool):
    password_rule = day_02.PasswordRuleCount(rule_string)
    assert password_rule.validate(password) is is_valid


@pytest.mark.parametrize(
    'rule_string,password,is_valid',
    [
        ('1-3 a', 'abcde', True),
        ('1-3 b', 'cdefg', False),
        ('2-9 c', 'ccccccccc', False),
        ('16-17 k', 'nphkpzqswcltkkbkk', False),
        ('8-11 l', 'qllllqllklhlvtl', True),
    ]
)
def test_password_rule_exists_validation(rule_string: str, password: str, is_valid: bool):
    password_rule = day_02.PasswordRuleExists(rule_string)
    assert password_rule.validate(password) is is_valid


@pytest.mark.parametrize(
    'password_string,is_valid',
    [
        ('1-3 a: abcde', True),
        ('1-3 b: cdefg', False),
        ('2-9 c: ccccccccc', False),
        ('16-17 k: nphkpzqswcltkkbkk', False),
        ('8-11 l: qllllqllklhlvtl', True),
    ]
)
def test_password_entry_exists_validation(password_string: str, is_valid: bool):
    password_entry = day_02.PasswordEntry(password_string, day_02.EXISTS)
    assert password_entry.is_valid() is is_valid
