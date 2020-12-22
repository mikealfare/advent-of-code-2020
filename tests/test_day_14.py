import pytest

from tests.conftest import day_14


sample_instructions = [
    'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
    'mem[8] = 11',
    'mem[7] = 101',
    'mem[8] = 0'
]


@pytest.mark.parametrize('value,mask,expected', [
    (11, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 73),
    (101, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 101),
    (0, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 64)
])
def test_get_masked_value(value, mask, expected):
    assert day_14.get_masked_value(value, mask) == expected


@pytest.mark.parametrize('instructions,expected', [
    (sample_instructions, {7: 101, 8: 64})
])
def test_execute_instructions(instructions, expected):
    assert day_14.execute_program(instructions) == expected


@pytest.mark.parametrize('address,mask,expected', [
    (42, '000000000000000000000000000000X1001X', [26, 27, 58, 59]),
    (26, '00000000000000000000000000000000X0XX', [16, 17, 18, 19, 24, 25, 26, 27])
])
def test_get_get_masked_addresses(address, mask, expected):
    assert sorted(day_14.get_masked_addresses(address, mask)) == expected
