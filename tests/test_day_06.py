from tests.conftest import day_06, PACKAGE_ROOT


def test_count_any():
    sample_file = PACKAGE_ROOT / 'static' / 'day_06.txt'
    forms = day_06.get_forms_from_file(sample_file.absolute())
    responses = [len(form.get_distinct_responses_any()) for form in forms]
    assert sum(responses) == 11


def test_count_all():
    sample_file = PACKAGE_ROOT / 'static' / 'day_06.txt'
    forms = day_06.get_forms_from_file(sample_file.absolute())
    responses = [len(form.get_distinct_responses_all()) for form in forms]
    assert sum(responses) == 6
