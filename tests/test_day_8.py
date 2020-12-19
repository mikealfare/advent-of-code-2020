from tests.conftest import day_8


sample_human_instructions = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6'
]
expected_instructions = {
    0: {'move': 1, 'acc': 0, 'human': {'mode': 'nop', 'amount': 0}},
    1: {'move': 1, 'acc': 1, 'human': {'mode': 'acc', 'amount': 1}},
    2: {'move': 4, 'acc': 0, 'human': {'mode': 'jmp', 'amount': 4}},
    3: {'move': 1, 'acc': 3, 'human': {'mode': 'acc', 'amount': 3}},
    4: {'move': -3, 'acc': 0, 'human': {'mode': 'jmp', 'amount': -3}},
    5: {'move': 1, 'acc': -99, 'human': {'mode': 'acc', 'amount': -99}},
    6: {'move': 1, 'acc': 1, 'human': {'mode': 'acc', 'amount': 1}},
    7: {'move': -4, 'acc': 0, 'human': {'mode': 'jmp', 'amount': -4}},
    8: {'move': 1, 'acc': 6, 'human': {'mode': 'acc', 'amount': 6}}
}
expected_fixed_instructions = {
    0: {'move': 1, 'acc': 0, 'human': {'mode': 'nop', 'amount': 0}},
    1: {'move': 1, 'acc': 1, 'human': {'mode': 'acc', 'amount': 1}},
    2: {'move': 4, 'acc': 0, 'human': {'mode': 'jmp', 'amount': 4}},
    3: {'move': 1, 'acc': 3, 'human': {'mode': 'acc', 'amount': 3}},
    4: {'move': -3, 'acc': 0, 'human': {'mode': 'jmp', 'amount': -3}},
    5: {'move': 1, 'acc': -99, 'human': {'mode': 'acc', 'amount': -99}},
    6: {'move': 1, 'acc': 1, 'human': {'mode': 'acc', 'amount': 1}},
    7: {'move': 1, 'acc': 0, 'human': {'mode': 'jmp', 'amount': -4}},  # this one
    8: {'move': 1, 'acc': 6, 'human': {'mode': 'acc', 'amount': 6}}
}


def test_convert_human_instructions_to_instructions_dict():
    assert day_8.convert_human_instructions_to_instructions_dict(sample_human_instructions) == expected_instructions


def test_get_accumulator_when_instructions_loop_or_complete():
    instructions = day_8.convert_human_instructions_to_instructions_dict(sample_human_instructions)
    assert day_8.get_accumulator_when_instructions_loop_or_complete(instructions) == (1, 5)


def test_get_fixed_instructions():
    instructions = day_8.convert_human_instructions_to_instructions_dict(sample_human_instructions)
    fixed_instructions = day_8.get_fixed_instructions(instructions, 7)
    assert fixed_instructions == expected_fixed_instructions
    original_instructions = day_8.convert_human_instructions_to_instructions_dict(sample_human_instructions)
    assert instructions == original_instructions


def test_get_accumulator_by_fixing_broken_instruction():
    instructions = day_8.convert_human_instructions_to_instructions_dict(sample_human_instructions)
    assert day_8.get_accumulator_by_fixing_broken_instruction(instructions) == 8
