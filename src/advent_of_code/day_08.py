from typing import List, Tuple, Dict, Union
from copy import deepcopy
from pathlib import Path


Line = int
Instructions = Dict[Line, Dict[str, Union[int, str]]]


def convert_human_instructions_to_instructions(human_instructions: List[str]) -> Instructions:
    result = {}
    for line, human_instruction in enumerate(human_instructions):
        mode, amount = human_instruction.strip().split(' ')
        instruction = {'mode': mode, 'amount': int(amount), 'move': 1, 'acc': 0}
        if mode == 'nop':
            pass
        elif mode == 'acc':
            instruction.update(acc=instruction['amount'])
        elif mode == 'jmp':
            instruction.update(move=instruction['amount'])
        else:
            raise ValueError('unsupported instruction mode')
        result[line] = instruction
    return result


def get_final_state(instructions: Instructions) -> Tuple[int, Line]:
    accumulator = 0
    executed_lines = set()
    next_line = 0
    while next_line not in executed_lines and next_line < len(instructions):
        accumulator += instructions[next_line]['acc']
        executed_lines.add(next_line)
        next_line += instructions[next_line]['move']
    return accumulator, next_line


def get_fixed_instructions(instructions: Instructions, line: Line) -> Instructions:
    fixed_instructions = deepcopy(instructions)
    instruction = fixed_instructions[line]
    if instruction['mode'] == 'jmp':
        instruction['move'] = 1
    elif instruction['mode'] == 'nop':
        instruction['move'] = instruction['amount']
    return fixed_instructions


def get_final_state_fixed(instructions: Instructions) -> Tuple[int, Line]:
    for line in instructions:
        if instructions[line]['mode'] in ['nop', 'jmp']:
            fixed_instructions = get_fixed_instructions(instructions, line)
            accumulator, next_line = get_final_state(fixed_instructions)
            if next_line == len(instructions):
                return accumulator, next_line


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_08.txt'):
    with open(file_path) as f:
        human_instructions = [line.strip() for line in f.readlines()]
    instructions = convert_human_instructions_to_instructions(human_instructions)
    accumulator, _ = get_final_state(instructions)
    print(f'the instructions loop with accumulator {accumulator}')
    fixed_accumulator, _ = get_final_state_fixed(instructions)
    print(f'the fixed instructions end with accumulator {fixed_accumulator}')


if __name__ == '__main__':
    main()
