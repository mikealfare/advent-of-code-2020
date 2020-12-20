from dataclasses import dataclass
from typing import List


@dataclass
class Passport:
    pid: str = None
    cid: str = None
    byr: str = None
    iyr: str = None
    eyr: str = None
    hgt: str = None
    hcl: str = None
    ecl: str = None

    def is_populated(self) -> bool:
        valid = (
            self.pid is not None and
            self.byr is not None and
            self.iyr is not None and
            self.eyr is not None and
            self.hgt is not None and
            self.hcl is not None and
            self.ecl is not None
        )
        return valid

    def is_valid_byr(self) -> bool:
        return int(self.byr) in range(1920, 2003)

    def is_valid_iyr(self) -> bool:
        return int(self.iyr) in range(2010, 2021)

    def is_valid_eyr(self) -> bool:
        return int(self.eyr) in range(2020, 2031)

    def is_valid_hgt(self) -> bool:
        if len(self.hgt) < 3:
            return False
        scalar = int(self.hgt[:-2])
        units = self.hgt[-2:]
        if units == 'cm':
            return scalar in range(150, 194)
        elif units == 'in':
            return scalar in range(59, 77)
        return False

    def is_valid_hcl(self) -> bool:
        if len(self.hcl) != 7:
            return False
        if self.hcl[0] != '#':
            return False
        for i in range(1, 7):
            if self.hcl[i] not in '0123456789abcdef':
                return False
        return True

    def is_valid_ecl(self) -> bool:
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_valid_pid(self) -> bool:
        if len(self.pid) != 9:
            return False
        test_pid = int(self.pid)
        return True

    def is_valid(self) -> bool:
        if not self.is_populated():
            return False
        return (
                self.is_valid_byr() and
                self.is_valid_eyr() and
                self.is_valid_iyr() and
                self.is_valid_hgt() and
                self.is_valid_hcl() and
                self.is_valid_ecl() and
                self.is_valid_pid()
        )


def get_passport_from_config_string(config_string: str) -> Passport:
    kwargs_string = config_string.replace('\n', ' ').strip()
    kwarg_strings = kwargs_string.split(' ')
    kwargs = {}
    for kwarg_string in kwarg_strings:
        key, value = kwarg_string.split(':')
        kwargs[key] = value
    return Passport(**kwargs)


def get_passports_from_file(file_path: str) -> List[Passport]:
    passports = []
    this_passport = ''
    with open(file_path) as f:
        for line in f.readlines():
            if line == '\n':
                passport = get_passport_from_config_string(this_passport)
                passports.append(passport)
                this_passport = ''
            else:
                this_passport += line
        if this_passport != '':
            passport = get_passport_from_config_string(this_passport)
            passports.append(passport)
    return passports


if __name__ == '__main__':
    all_passports = get_passports_from_file('input_files/day_04.txt')
    populated_passports = [passport for passport in all_passports if passport.is_populated()]
    print(f'There are {len(populated_passports)} populated passports')
    valid_passports = [passport for passport in all_passports if passport.is_valid()]
    print(f'There are {len(valid_passports)} valid passports')
