from copy import deepcopy
from typing import List

import numpy as np


def parse_input() -> List[List[int]]:
    """Parse input"""
    with open("./data/day_11.txt") as f:
        occ = [[0 if c == "L" else np.nan for c in line.strip()] for line in f]

    return occ


def part_one(occ):
    while True:
        occ_new = deepcopy(occ)
        for x in range(len(occ)):
            for y in range(len(occ[x])):
                if occupy(occ, x, y):
                    occ_new[x][y] = 1
                elif release(occ, x, y):
                    occ_new[x][y] = 0
        if occ_new == occ:
            break
        occ = occ_new

    return int(np.nansum(occ))


def part_two(occ):
    while True:
        occ_new = deepcopy(occ)
        for x in range(len(occ)):
            for y in range(len(occ[x])):
                if occupy_part_two(occ, x, y):
                    occ_new[x][y] = 1
                elif release_part_two(occ, x, y):
                    occ_new[x][y] = 0
        if occ_new == occ:
            break
        occ = occ_new

    return int(np.nansum(occ))


def adjacent(occ, x, y):
    return [
        occ[i][max(0, y - 1) : min(y + 2, len(occ[i]))]
        for i in range(max(0, x - 1), min(x + 2, len(occ)))
    ]


def occupy(occ, x, y):
    return occ[x][y] == 0 and np.nansum(adjacent(occ, x, y)) == 0


def release(occ, x, y):
    return occ[x][y] == 1 and np.nansum(adjacent(occ, x, y)) >= 5


def adjacent_part_two(occ, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    return [find_seat(occ, x, y, d) for d in directions]


def find_seat(occ, x, y, d):
    i = x + d[0]
    j = y + d[1]

    if i in range(len(occ)):
        if j in range(len(occ[i])):
            if not np.isnan(occ[i][j]):
                return occ[i][j]
            return find_seat(occ, i, j, d)
    return 0


def occupy_part_two(occ, x, y):
    return occ[x][y] == 0 and sum(adjacent_part_two(occ, x, y)) == 0


def release_part_two(occ, x, y):
    return occ[x][y] == 1 and sum(adjacent_part_two(occ, x, y)) >= 5


if __name__ == "__main__":
    occ = parse_input()
    # print(adjacent_part_two(occ, 0, 0))
    r_1 = part_one(occ)
    print(f"Result part one: {r_1}")
    # occ = parse_input()
    r_2 = part_two(occ)
    print(f"Result part two: {r_2}")
    # print(adjacent_part_two(
    #     [
    #         [0, 0, 1, 0, 1],
    #         [1, 0, np.nan, np.nan],
    #         [0, np.nan, 0, np.nan, 1],
    #         [1, 1, 1, 1, 1]
    #     ], 2, 2
    # ))
