from typing import List, Set


class Form:

    def __init__(self, form_string: str):
        form_entries_string = form_string.replace('\n', ' ').strip()
        self.entries = [entry for entry in form_entries_string.split(' ')]

    def get_distinct_responses_any(self) -> Set[str]:
        return {char for char in ''.join(self.entries)}

    def get_distinct_responses_all(self) -> Set[str]:
        all_responses = {char for char in self.entries[0]}
        for i in range(1, len(self.entries)):
            all_responses = all_responses.intersection({char for char in self.entries[i]})
        return all_responses


def get_forms_from_file(file_path: str) -> List[Form]:
    forms = []
    this_form = ''
    with open(file_path) as f:
        for line in f.readlines():
            if line == '\n':
                forms.append(Form(this_form))
                this_form = ''
            else:
                this_form += line
        if this_form != '':
            forms.append(Form(this_form))
    return forms


if __name__ == '__main__':
    forms = get_forms_from_file('input_files/day_06.txt')
    any_responses = [len(form.get_distinct_responses_any()) for form in forms]
    print(f'There are {sum(any_responses)} responses for anyone in a group')
    all_responses = [len(form.get_distinct_responses_all()) for form in forms]
    print(f'There are {sum(all_responses)} responses for all in a group')
