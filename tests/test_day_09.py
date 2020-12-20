import pytest

from tests.conftest import day_09


sample_port_numbers = [
    35, 20, 15, 25, 47,
    40, 62, 55, 65, 95,
    102, 117, 150, 182, 127,
    219, 299, 277, 309, 576
]


@pytest.mark.parametrize('port_numbers,preamble,expected', [(sample_port_numbers, 5, 127)])
def test_find_first_error(port_numbers, preamble, expected):
    assert day_09.find_first_error(port_numbers=port_numbers, preamble=preamble) == expected


@pytest.mark.parametrize('port_numbers,target_sum,expected', [(sample_port_numbers, 127, [15, 25, 47, 40])])
def test_find_first_error(port_numbers, target_sum, expected):
    assert day_09.find_contiguous_numbers_adding_to_provided_sum(port_numbers, target_sum) == expected
