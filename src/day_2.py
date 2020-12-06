"""Solution for day 2.

Part 1:
Count the number of correct passwords. Each line contains the policy and then a password
Policy is always a min and max occurence of the letter following

Part 2:
Count the number of correct passwords. Each line contains the policy and then a password
Policy indicates positions
"""


def parse_input():
    """Parse the input of this problem."""
    with open("./data/day_2.txt", "r") as f:
        lines = f.read().split("\n")
    # data is a tuple min max letter pw
    data = []
    for line in lines:
        pol, pw = line.split(": ")
        minmax, letter = pol.split(" ")
        mn, mx = (int(x) for x in minmax.split("-"))
        data.append((mn, mx, letter, pw))

    return data


def part_one():
    """Execute part 1."""
    data = parse_input()
    count = 0
    for entry in data:
        l_count = 0
        for letter in entry[3]:
            if letter == entry[2]:
                l_count += 1
        if l_count >= entry[0] and l_count <= entry[1]:
            count += 1

    print(count)


def part_two():
    """Execute part 2."""
    data = parse_input()
    count = 0
    for entry in data:
        first = entry[0] - 1
        second = entry[1] - 1
        letter = entry[2]
        pw = entry[3]
        if pw[first] == letter:
            if pw[second] != letter:
                count += 1
        elif pw[second] == letter:
            count += 1

    print(count)


if __name__ == "__main__":
    part_one()
    part_two()
