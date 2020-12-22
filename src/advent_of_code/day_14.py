from typing import List
from copy import deepcopy


def get_masked_value(value: int, mask: str) -> int:
    binary_chars = [char for char in str(bin(value))[2:].zfill(36)]
    for spot, value in enumerate(mask):
        if value != 'X':
            binary_chars[spot] = value
    return int(''.join(binary_chars), 2)


def update_memory(memory: dict, write_instruction: str, mask: str):
    address = int(write_instruction.split('[')[1].split(']')[0])
    value = int(write_instruction.split(' ')[-1])
    memory.update({address: get_masked_value(value, mask)})


def execute_program(instructions: List[str]) -> dict:
    memory = {}
    mask = ''
    for instruction in instructions:
        if instruction[:4] == 'mask':
            mask = instruction.split(' ')[-1]
        elif instruction[:3] == 'mem':
            update_memory(memory, instruction, mask)
        else:
            raise ValueError('ERROR - unsupported instruction')
    return memory


def get_masked_addresses(unmasked_address: int, mask: str) -> List[int]:
    addresses = [[char for char in str(bin(unmasked_address))[2:].zfill(36)], ]
    for spot, value in enumerate(mask):
        if value == '1':
            for address in addresses:
                address[spot] = '1'
        elif value == 'X':
            for address in addresses:
                address[spot] = '0'
            dupe_addresses = deepcopy(addresses)
            for address in dupe_addresses:
                address[spot] = '1'
            addresses.extend(dupe_addresses)
    return [int(''.join(address), 2) for address in addresses]


def update_memory_version_2(memory: dict, write_instruction: str, mask: str):
    unmasked_address = int(write_instruction.split('[')[1].split(']')[0])
    masked_addresses = get_masked_addresses(unmasked_address, mask)
    value = int(write_instruction.split(' ')[-1])
    for address in masked_addresses:
        memory.update({address: value, })


def execute_program_version_2(instructions: List[str]) -> dict:
    memory = {}
    mask = ''
    for instruction in instructions:
        if instruction[:4] == 'mask':
            mask = instruction.split(' ')[-1]
        elif instruction[:3] == 'mem':
            update_memory_version_2(memory, instruction, mask)
        else:
            raise ValueError('ERROR - unsupported instruction')
    return memory


def main():
    with open('input_files/day_14.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    memory = execute_program(instructions)
    print(f'the sum left in memory is {sum(memory.values())}')
    memory_v2 = execute_program_version_2(instructions)
    print(f'the sum left in memory in version 2 is {sum(memory_v2.values())}')


if __name__ == '__main__':
    main()

