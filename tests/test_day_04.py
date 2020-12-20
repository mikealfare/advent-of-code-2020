from tests.conftest import day_04, PACKAGE_ROOT


sample_passport_string_full = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm'''

sample_passport_string_missing_height = '''iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929'''


def test_get_passport_from_config_string_full():
    passport = day_04.get_passport_from_config_string(config_string=sample_passport_string_full)
    assert passport.pid == '860033327'
    assert passport.cid == '147'
    assert passport.byr == '1937'
    assert passport.iyr == '2017'
    assert passport.eyr == '2020'
    assert passport.hgt == '183cm'
    assert passport.hcl == '#fffffd'
    assert passport.ecl == 'gry'


def test_get_passport_from_config_string_missing_height():
    passport = day_04.get_passport_from_config_string(config_string=sample_passport_string_missing_height)
    assert passport.pid == '028048884'
    assert passport.cid == '350'
    assert passport.byr == '1929'
    assert passport.iyr == '2013'
    assert passport.eyr == '2023'
    assert passport.hgt is None
    assert passport.hcl == '#cfa07d'
    assert passport.ecl == 'amb'


def test_get_passports_from_file():
    sample_file = PACKAGE_ROOT / 'static' / 'day_04.txt'
    passports = day_04.get_passports_from_file(sample_file.absolute())
    passport_ids = [passport.pid for passport in passports]
    assert passport_ids == ['860033327', '028048884', '760753108', '166559648']


def test_get_populated_passport_count():
    sample_file = PACKAGE_ROOT / 'static' / 'day_04.txt'
    passports = day_04.get_passports_from_file(sample_file.absolute())
    populated_passports = [passport for passport in passports if passport.is_populated()]
    assert len(populated_passports) == 2
