from pathlib import Path

import pytest

from tests.conftest import day_04, PACKAGE_ROOT


@pytest.fixture
def sample_passport_file() -> Path:
    return PACKAGE_ROOT / 'static' / 'day_04.txt'


@pytest.mark.parametrize('config_string,expected', [
    ('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
     day_04.Passport(
         pid='860033327',
         cid='147',
         byr='1937',
         iyr='2017',
         eyr='2020',
         hgt='183cm',
         hcl='#fffffd',
         ecl='gry'
     )),
    ('iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929',
     day_04.Passport(
         pid='028048884',
         cid='350',
         byr='1929',
         iyr='2013',
         eyr='2023',
         hcl='#cfa07d',
         ecl='amb'
     )),
])
def test_get_passport_from_config_string(config_string: str, expected: day_04.Passport):
    assert day_04.get_passport_from_config_string(config_string) == expected


def test_get_passports_from_file(sample_passport_file):
    passports = day_04.get_passports_from_file(sample_passport_file)
    passport_ids = [passport.pid for passport in passports]
    assert passport_ids == ['860033327', '028048884', '760753108', '166559648']
    populated_passports = [passport for passport in passports if passport.is_populated]
    assert len(populated_passports) == 2
