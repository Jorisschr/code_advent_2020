from math import cos, pi, sin
from typing import List, Tuple


def parse_input() -> List[Tuple[str, int]]:
    """Parse the input"""
    with open("./data/day_12.txt") as f:
        lines = [(l[0], int(l[1:])) for l in f]

    return lines


def part_one(commands: List[Tuple[str, int]]) -> int:
    """Execute part one.

    Parameters
    ----------
    commands : List[Tuple[str, int]]
        parsed input

    Returns
    -------
    int
        manhattan distance between pos and (0, 0)
    """
    direction = 0
    pos = (0, 0)

    for c in commands:
        d = moves_part_one[c[0]]
        if callable(d):
            direction, pos = d(direction, pos, c[1])
        else:
            pos = (pos[0] + d[0] * c[1], pos[1] + d[1] * c[1])

    return manhattan(pos)


def part_two(commands: List[Tuple[str, int]]) -> int:
    """Execute part two.

    Parameters
    ----------
    commands : List[Tuple[str, int]]
        parsed input

    Returns
    -------
    int
        manhattan distance between pos and (0, 0)
    """
    waypoint = (10, 1)
    pos = (0, 0)

    for c in commands:
        d = moves_part_two[c[0]]
        if callable(d):
            pos, waypoint = d(pos, waypoint, c[1])
        else:
            waypoint = (waypoint[0] + d[0] * c[1], waypoint[1] + d[1] * c[1])

    return manhattan(pos)


def manhattan(pos: Tuple[int, int]) -> int:
    return sum((abs(x) for x in pos))


def left_part_one(
    d: int, pos: Tuple[int, int], step: int
) -> Tuple[int, Tuple[int, int]]:
    d = (d + (step // 90)) % 4
    return d, pos


def right_part_one(
    d: int, pos: Tuple[int, int], step: int
) -> Tuple[int, Tuple[int, int]]:
    d = (d - (step // 90)) % 4
    return d, pos


def forward_part_one(
    d: int, pos: Tuple[int, int], step: int
) -> Tuple[int, Tuple[int, int]]:
    pos = (
        pos[0] + (direction[d][0] * step),
        pos[1] + (direction[d][1] * step),
    )
    return d, pos


def left_part_two(
    pos: Tuple[int, int], wp: Tuple[int, int], step: int
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    rad = step / 180 * pi
    wp = (
        int(cos(rad)) * wp[0] - int(sin(rad)) * wp[1],
        int(sin(rad)) * wp[0] + int(cos(rad)) * wp[1],
    )
    return pos, wp


def right_part_two(
    pos: Tuple[int, int], wp: Tuple[int, int], step: int
) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    return left_part_two(pos, wp, -step)


def forward_part_two(pos: Tuple[int, int], wp: Tuple[int, int], step: int):
    pos = (pos[0] + (wp[0] * step), pos[1] + (wp[1] * step))
    return pos, wp


moves_part_one = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
    "L": left_part_one,
    "R": right_part_one,
    "F": forward_part_one,
}

moves_part_two = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
    "L": left_part_two,
    "R": right_part_two,
    "F": forward_part_two,
}

direction = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


if __name__ == "__main__":
    commands = parse_input()
    r_1 = part_one(commands)
    print(f"Result part one: {r_1}")
    r_2 = part_two(commands)
    print(f"Result part two: {r_2}")
