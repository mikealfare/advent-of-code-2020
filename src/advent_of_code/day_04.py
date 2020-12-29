from dataclasses import dataclass
from typing import List
from pathlib import Path


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

    @property
    def is_populated(self) -> bool:
        return all([self.pid, self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl])

    @property
    def is_valid_byr(self) -> bool:
        return int(self.byr) in range(1920, 2003)

    @property
    def is_valid_iyr(self) -> bool:
        return int(self.iyr) in range(2010, 2021)

    @property
    def is_valid_eyr(self) -> bool:
        return int(self.eyr) in range(2020, 2031)

    @property
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

    @property
    def is_valid_hcl(self) -> bool:
        if len(self.hcl) != 7:
            return False
        if self.hcl[0] != '#':
            return False
        return all([char in '0123456789abcdef' for char in self.hcl[1:]])

    @property
    def is_valid_ecl(self) -> bool:
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    @property
    def is_valid_pid(self) -> bool:
        if len(self.pid) != 9:
            return False
        try:
            test_pid = int(self.pid)
        except ValueError:
            return False
        return True

    @property
    def is_valid(self) -> bool:
        if not self.is_populated:
            return False
        return all([
            self.is_valid_byr,
            self.is_valid_eyr,
            self.is_valid_iyr,
            self.is_valid_hgt,
            self.is_valid_hcl,
            self.is_valid_ecl,
            self.is_valid_pid
        ])


def get_passport_from_config_string(config_string: str) -> Passport:
    kwarg_strings = config_string.split(' ')
    kwargs = {}
    for kwarg_string in kwarg_strings:
        key, value = kwarg_string.split(':')
        kwargs[key] = value
    return Passport(**kwargs)


def get_passports_from_file(file_path: Path) -> List[Passport]:
    passports = ['']
    with open(file_path) as f:
        for line in f.readlines():
            if line.strip() == '':
                passports.append('')
            else:
                passports[-1] = ' '.join([passports[-1], line]).strip()
    return [get_passport_from_config_string(passport) for passport in passports]


def main(file_path: Path = Path(__file__).parent / 'input_files' / 'day_04.txt'):
    all_passports = get_passports_from_file(file_path)
    populated_passports = [passport for passport in all_passports if passport.is_populated]
    print(f'There are {len(populated_passports)} populated passports')
    valid_passports = [passport for passport in all_passports if passport.is_valid]
    print(f'There are {len(valid_passports)} valid passports')


if __name__ == '__main__':
    main()
