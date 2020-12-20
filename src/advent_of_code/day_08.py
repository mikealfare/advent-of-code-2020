from typing import List, Tuple
from copy import deepcopy


def convert_human_instructions_to_instructions_dict(human_instructions: List[str]) -> dict:
    result = {}
    for i, instruction in enumerate(human_instructions):
        mode, amount = instruction.strip().split(' ')
        if mode == 'nop':
            step = {'move': 1, 'acc': 0, 'human': {'mode': 'nop', 'amount': int(amount)}}
        elif mode == 'acc':
            step = {'move': 1, 'acc': int(amount), 'human': {'mode': 'acc', 'amount': int(amount)}}
        elif mode == 'jmp':
            step = {'move': int(amount), 'acc': 0, 'human': {'mode': 'jmp', 'amount': int(amount)}}
        else:
            raise ValueError('unsupported instruction mode')
        result[i] = step
    return result


def get_accumulator_when_instructions_loop_or_complete(instructions: dict) -> Tuple[int, int]:
    executed_steps = []
    next_step = 0
    accumulator = 0
    while True:
        if next_step in executed_steps or next_step >= len(instructions):
            return next_step, accumulator
        accumulator += instructions[next_step]['acc']
        executed_steps.append(next_step)
        next_step += instructions[next_step]['move']


def get_fixed_instructions(instructions: dict, step: int) -> dict:
    mode = instructions[step]['human']['mode']
    fixed_instructions = deepcopy(instructions)
    if mode == 'jmp':
        fixed_instructions[step]['move'] = 1
        return fixed_instructions
    if mode == 'nop':
        fixed_instructions[step]['move'] = instructions[step]['human']['amount']
        return fixed_instructions
    return fixed_instructions


def get_accumulator_by_fixing_broken_instruction(instructions: dict) -> int:
    for step in instructions:
        mode = instructions[step]['human']['mode']
        if mode in ['nop', 'jmp']:
            fixed_instructions = get_fixed_instructions(instructions, step)
            next_step, accumulator = get_accumulator_when_instructions_loop_or_complete(fixed_instructions)
            if next_step == len(instructions):
                return accumulator


def main():
    with open('input_files/day_08.txt') as f:
        human_instructions = [line.replace('\n', '') for line in f.readlines()]
    instructions = convert_human_instructions_to_instructions_dict(human_instructions=human_instructions)
    _, accumulator = get_accumulator_when_instructions_loop_or_complete(instructions)
    print(f'the instructions loop with accumulator {accumulator}')
    fixed_accumulator = get_accumulator_by_fixing_broken_instruction(instructions)
    print(f'the accumulator for the fixed instructions is {fixed_accumulator}')


if __name__ == '__main__':
    main()
