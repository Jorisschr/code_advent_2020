"""Solution for day 6.

Part 1:
Count the number of unique letters per group

Part 2:
Count the number of common letters among every line of a group
"""

from functools import reduce

def parse_input():
    """Parse the input of this problem."""
    with open("./data/day_6.txt", 'r') as f:
        groups = f.read().split("\n\n")
        groups = [g.replace("\n", "") for g in groups]

    return groups


def part_one():
    """Execute part 1."""
    groups = parse_input()
    res = sum([len(set(group)) for group in groups])
    print(res)


def part_two():
    """Execute part 2."""
    with open("./data/day_6.txt", 'r') as f:
        groups = f.read().split("\n\n")
    result = 0
    for group in groups:
        lines = group.split("\n")
        sets = [set(l) for l in lines]
        final_set = reduce(lambda x, y: x.intersection(y), sets)
        result += len(final_set)
    print(result)



if __name__ == "__main__":
    part_one()
    part_two()
