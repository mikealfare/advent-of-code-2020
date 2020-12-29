from typing import List

import pytest

from tests.conftest import day_06, PACKAGE_ROOT


@pytest.fixture
def sample_forms() -> List[day_06.Form]:
    forms_file = PACKAGE_ROOT / 'static' / 'day_06.txt'
    return day_06.get_forms_from_file(forms_file)


def test_get_distinct_responses_any(sample_forms: List[day_06.Form]):
    responses = [day_06.get_distinct_responses_any(form) for form in sample_forms]
    assert sum(responses) == 11


def test_get_distinct_responses_all(sample_forms: List[day_06.Form]):
    responses = [day_06.get_distinct_responses_all(form) for form in sample_forms]
    assert sum(responses) == 6
