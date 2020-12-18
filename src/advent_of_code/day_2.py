from enum import Enum


COUNT = 0
EXISTS = 1


class PasswordEntry:

    def __init__(self, password_entry: str, validation_scheme: int):
        self.password_entry = password_entry
        rule_string, password = password_entry.split(':')
        self.password = password.strip()
        if validation_scheme == COUNT:
            self.password_rule = PasswordRuleCount(rule_string)
        elif validation_scheme == EXISTS:
            self.password_rule = PasswordRuleExists(rule_string)
        else:
            raise ValueError('Unsupported validation rule scheme')

    def is_valid(self) -> bool:
        return self.password_rule.validate(self.password)


class PasswordRuleCount:

    def __init__(self, rule_string: str):
        requirement_range, self.letter = rule_string.split(' ')
        min_occ, max_occ = requirement_range.split('-')
        self.minimum_occurrences = int(min_occ)
        self.maximum_occurrences = int(max_occ)

    def validate(self, password: str) -> bool:
        occurrences = password.count(self.letter)
        return (self.minimum_occurrences <= occurrences) & (occurrences <= self.maximum_occurrences)


class PasswordRuleExists:

    def __init__(self, rule_string: str):
        requirement_occurrences, self.letter = rule_string.split(' ')
        first_occurrence, second_occurrence = requirement_occurrences.split('-')
        self.first_occurrence = int(first_occurrence)-1
        self.second_occurrence = int(second_occurrence)-1

    def validate(self, password: str) -> bool:
        occurrences = [password[self.first_occurrence], password[self.second_occurrence]]
        valid_occurrences = [occurrence for occurrence in occurrences if occurrence == self.letter]
        is_valid_by_count = (len(valid_occurrences) == 1)

        is_valid_first = False
        is_valid_second = False
        if password[self.first_occurrence] == self.letter:
            is_valid_first = True
        if password[self.second_occurrence] == self.letter:
            is_valid_second = True
        is_valid_by_eval = (is_valid_first != is_valid_second)

        return is_valid_by_eval


if __name__ == '__main__':
    with open('input_files/day_2.txt') as f:
        password_entries = [line.replace('\n', '') for line in f.readlines()]
    passwords = [PasswordEntry(password_entry=entry, validation_scheme=EXISTS) for entry in password_entries]
    valid_passwords = [password for password in passwords if password.is_valid()]
    valid_password_entries = [pw.password_entry for pw in valid_passwords]
    print(f'valid_password_count: {len(valid_passwords)}; entries: {valid_password_entries}')
