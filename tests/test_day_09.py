from typing import List

import pytest

from tests.conftest import day_09


sample_port_numbers = [
    35, 20, 15, 25, 47,
    40, 62, 55, 65, 95,
    102, 117, 150, 182, 127,
    219, 299, 277, 309, 576
]


@pytest.mark.parametrize('port_numbers,preamble,expected', [(sample_port_numbers, 5, 127)])
def test_find_first_error(port_numbers: List[day_09.PortNumber], preamble: int, expected: day_09.PortNumber):
    assert day_09.find_first_error(port_numbers, preamble) == expected


@pytest.mark.parametrize('port_numbers,target_sum,expected', [(sample_port_numbers, 127, [15, 25, 47, 40])])
def test_find_contiguous_numbers_adding_to_target_sum(
        port_numbers: List[day_09.PortNumber],
        target_sum: int,
        expected: List[day_09.PortNumber]
):
    assert day_09.find_contiguous_numbers_adding_to_target_sum(port_numbers, target_sum) == expected
