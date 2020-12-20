from tests.conftest import day_01


def test_get_permutations():
    entries = {30, 40, 50}
    length = 2
    expected = {(30, 40), (30, 50), (40, 50)}
    actual = day_01.get_permutations(entries=entries, length=length)
    assert actual == expected


def test_get_permutations_with_sum_limit():
    entries = {30, 40, 50}
    length = 2
    sum_limit = 70
    expected = {(30, 40)}
    actual = day_01.get_permutations_with_sum_limit(entries=entries, length=length, sum_limit=sum_limit)
    assert actual == expected
