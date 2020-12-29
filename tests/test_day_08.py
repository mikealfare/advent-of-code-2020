from typing import List

import pytest

from tests.conftest import day_08


@pytest.fixture
def sample_instructions() -> day_08.Instructions:
    instructions = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6']
    return day_08.convert_human_instructions_to_instructions(instructions)


@pytest.mark.parametrize('human_instructions,expected', [
    ([
        'nop +0',
        'acc +1',
        'jmp +4',
        'acc +3',
        'jmp -3',
        'acc -99',
        'acc +1',
        'jmp -4',
        'acc +6'
     ],
     {
        0: {'move': 1, 'acc': 0, 'mode': 'nop', 'amount': 0},
        1: {'move': 1, 'acc': 1, 'mode': 'acc', 'amount': 1},
        2: {'move': 4, 'acc': 0, 'mode': 'jmp', 'amount': 4},
        3: {'move': 1, 'acc': 3, 'mode': 'acc', 'amount': 3},
        4: {'move': -3, 'acc': 0, 'mode': 'jmp', 'amount': -3},
        5: {'move': 1, 'acc': -99, 'mode': 'acc', 'amount': -99},
        6: {'move': 1, 'acc': 1, 'mode': 'acc', 'amount': 1},
        7: {'move': -4, 'acc': 0, 'mode': 'jmp', 'amount': -4},
        8: {'move': 1, 'acc': 6, 'mode': 'acc', 'amount': 6}
    })
])
def test_convert_human_instructions_to_instructions(human_instructions: List[str], expected: day_08.Instructions):
    assert day_08.convert_human_instructions_to_instructions(human_instructions) == expected


@pytest.mark.parametrize('expected_acc,expected_next_line', [(5, 1)])
def test_get_final_state(
        sample_instructions: day_08.Instructions,
        expected_acc: int,
        expected_next_line: day_08.Line
):
    assert day_08.get_final_state(sample_instructions) == (expected_acc, expected_next_line)


@pytest.mark.parametrize('line,expected', [
    (7, {
        0: {'move': 1, 'acc': 0, 'mode': 'nop', 'amount': 0},
        1: {'move': 1, 'acc': 1, 'mode': 'acc', 'amount': 1},
        2: {'move': 4, 'acc': 0, 'mode': 'jmp', 'amount': 4},
        3: {'move': 1, 'acc': 3, 'mode': 'acc', 'amount': 3},
        4: {'move': -3, 'acc': 0, 'mode': 'jmp', 'amount': -3},
        5: {'move': 1, 'acc': -99, 'mode': 'acc', 'amount': -99},
        6: {'move': 1, 'acc': 1, 'mode': 'acc', 'amount': 1},
        7: {'move': 1, 'acc': 0, 'mode': 'jmp', 'amount': -4},
        8: {'move': 1, 'acc': 6, 'mode': 'acc', 'amount': 6}
    })
])
def test_get_fixed_instructions(
        sample_instructions: day_08.Instructions,
        line: day_08.Line,
        expected: day_08.Instructions
):
    assert day_08.get_fixed_instructions(sample_instructions, line) == expected


@pytest.mark.parametrize('expected', [8])
def test_get_final_state_fixed(sample_instructions: day_08.Instructions, expected: int):
    assert day_08.get_final_state_fixed(sample_instructions) == (expected, len(sample_instructions))
