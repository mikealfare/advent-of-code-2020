from typing import List, Set
from pathlib import Path
from functools import reduce


Entry = Set[str]
Form = List[Entry]


def get_distinct_responses_any(form: Form) -> int:
    return len(reduce(lambda x, y: x.union(y), form))


def get_distinct_responses_all(form: Form) -> int:
    return len(reduce(lambda x, y: x.intersection(y), form))


def get_forms_from_file(file_path: Path) -> List[Form]:
    forms = [[]]
    with open(file_path) as f:
        for entry in f.readlines():
            if entry.strip() == '':
                forms.append([])
            else:
                forms[-1].append({char for char in entry.strip()})
    return forms


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_06.txt'):
    forms = get_forms_from_file(file_path)
    any_responses = [get_distinct_responses_any(form) for form in forms]
    print(f'There are {sum(any_responses)} responses for anyone in a group')
    all_responses = [get_distinct_responses_all(form) for form in forms]
    print(f'There are {sum(all_responses)} responses for all in a group')


if __name__ == '__main__':
    main()
