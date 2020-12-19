from tests.conftest import day_6, PACKAGE_ROOT


def test_count_any():
    sample_file = PACKAGE_ROOT / 'static' / 'day_6.txt'
    forms = day_6.get_forms_from_file(sample_file.absolute())
    responses = [len(form.get_distinct_responses_any()) for form in forms]
    assert sum(responses) == 11


def test_count_all():
    sample_file = PACKAGE_ROOT / 'static' / 'day_6.txt'
    forms = day_6.get_forms_from_file(sample_file.absolute())
    responses = [len(form.get_distinct_responses_all()) for form in forms]
    assert sum(responses) == 6
