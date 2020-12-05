"""Solution for day 4.

Part 1:
Parse the given list of passports and count the ones that contain at least all mandatory fields.

Part 2:
Check whether the given passports are valid.
"""

import re

required = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
]


def part_one():
    """Solve part 1."""
    with open("./data/day_4.txt", 'r') as f:
            lines = f.read().split("\n\n")

    count = 0
    for pp in lines:
        passport = {}

        for line in pp.split("\n"):

            for entry in line.split(" "):

                key, value = entry.split(":")
                passport[key] = value
        if len([x for x in required if x in passport.keys()]) == 7:
            count += 1

    print(count)


def part_two():
    """Solve part 2."""
    with open("./data/day_4.txt", 'r') as f:
            lines = f.read().split("\n\n")
    count = 0
    for pp in lines:
        passport = {}

        for line in pp.split("\n"):

            for entry in line.split(" "):

                key, value = entry.split(":")
                passport[key] = value
        try:
            valid(passport)
            count += 1
        except Exception:
            pass

    print(count)


def valid(passport):
    """Assert the given passport is valid.

    Parameters
    ----------
    passport : dict
        dictionary representing a passport
    """
    assert len([x for x in required if x in passport.keys()]) == 7
    assert int(passport["byr"]) >= 1920
    assert int(passport["byr"]) <= 2002
    assert int(passport["iyr"]) >= 2010
    assert int(passport["iyr"]) <= 2020
    assert int(passport["eyr"]) >= 2020
    assert int(passport["eyr"]) <= 2030
    assert passport["hgt"].endswith("cm") or passport["hgt"].endswith("in")
    if passport["hgt"].endswith("cm"):
        assert int(passport["hgt"][:-2]) >= 150
        assert int(passport["hgt"][:-2]) <= 193
    else:
        assert int(passport["hgt"][:-2]) >= 59
        assert int(passport["hgt"][:-2]) <= 76

    assert re.match(r"^\#[a-f0-9]{6}$", passport["hcl"])
    assert passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    assert re.match(r"^\d{9}$", passport["pid"])


if __name__ == "__main__":
    part_one()
    part_two()
