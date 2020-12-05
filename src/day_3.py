"""Solution for day 3.

Part 1:
Count the number of trees you pass through given a slope (for example 3 right, 1 down)

Part 2:
Check all given slopes and multiply the result
"""
from functools import reduce


def parse_input():
    """Parse the input of this problem."""
    with open("./data/day_3.txt", 'r') as f:
        lines = f.read().split("\n")

    return lines


def part_one(down, right, pos=(0, 0)):
    """Execute part 1."""
    lines = parse_input()

    count = 0
    while pos[0] < len(lines):
        if lines[pos[0]][pos[1]] == "#":
            count += 1
        pos = (
            pos[0] + down,
            (pos[1] + right) % len(lines[pos[0]])
        )

    print(count)
    return count


def part_two(slopes):
    """Execute part 2."""
    counts = [part_one(*slope) for slope in slopes]
    print(counts)
    return reduce(lambda x, y: x * y, counts)


if __name__ == "__main__":
    part_one(1, 3)
    slopes = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
    print(part_two(slopes))
