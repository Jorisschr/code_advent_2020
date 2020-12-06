"""Solution for day 1.

Part 1:
Find the two entries that sum to 2020, multiply and return the result.

Part 2:
Find the three entries that sum to 2020, multiply and return the result.
"""


def part_one():
    """Execute part 1."""
    with open("./data/day_1.txt", "r") as f:
        data = [int(x) for x in f.read().split("\n")]

    for x in range(len(data[:-1])):
        for y in range(x, len(data)):
            if data[x] + data[y] == 2020:
                print(data[x], data[y], data[x] * data[y])


def part_two():
    """Execute part 2."""
    with open("./data/day_1.txt", "r") as f:
        data = [int(x) for x in f.read().split("\n")]

    for x in range(len(data[:-2])):
        for y in range(x, len(data[:-1])):
            for z in range(y, len(data)):
                if data[x] + data[y] + data[z] == 2020:
                    print(data[x], data[y], data[z], data[x] * data[y] * data[z])


if __name__ == "__main__":
    part_one()
    part_two()
