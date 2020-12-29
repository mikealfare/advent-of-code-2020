import pytest

from tests.conftest import day_01


@pytest.mark.parametrize('entries,sum_limit,expected', [({30, 40, 50}, 70, 1200)])
def test_get_permutations_with_sum_limit(entries: day_01.Expenses, sum_limit: int, expected: int):
    assert day_01.get_product_of_combinations_with_sum_limit(entries, sum_limit) == expected
