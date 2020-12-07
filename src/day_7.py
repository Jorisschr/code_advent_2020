"""Solution for day 7.

Part 1:
Count the amount of bags that are required to contain a shiny gold bag.

Part 2:
Count the amount of bags required to be inside a shiny gold bag.
"""


def parse_input():
    """Parse the input of this problem."""
    with open("./data/day_7.txt", "r") as f:
        lines = f.read().split("\n")

    rules = {}
    for line in lines:
        bag, content = line.split(" bags contain ")
        contents = content.replace(".", "").replace(" bags", "").replace(" bag", "").split(", ")
        tups = []
        for c in contents:
            try:
                n = int(c[:c.index(" ")])
                color = c[c.index(" ") + 1:]
                tups.append((n, color))

            except Exception:
                # If no other bags inside
                tups.append((0, color))
        rules[bag] = tups

    return rules


def part_one(bags={"shiny gold"}):
    """Execute part 1."""
    original_len = len(bags)
    rules = parse_input()

    to_check = set(rules.keys())
    checked = set()

    while len(to_check) > 0:
        key = to_check.pop()

        if key not in bags:

            content = rules[key]
            for el in content:
                if el[1] in bags and el[0] > 0:
                    bags.add(key)
                    to_check = to_check.union(checked)
                    checked = set()

            if key not in bags:
                checked.add(key)

    print(len(bags) - original_len)


def part_two():
    """Execute part 2."""
    rules = parse_input()
    print(amount_of_bags(rules, "shiny gold"))


def amount_of_bags(rules: dict, bag: str) -> int:
    """Count the required amount of bags in the given bag according to the rules.

    Parameters
    ----------
    rules : dict
        dictionary containing the ruls
    bag : str
        name of a bag color

    Returns
    -------
    int
        number of bags required bags inside the given bag.
    """
    content = rules[bag]

    return sum(
        [
            content[i][0] * (amount_of_bags(rules, content[i][1]) + 1)
            for i in range(len(content)) if content[i][0] > 0
        ]
    )


if __name__ == "__main__":
    part_one()
    part_two()
