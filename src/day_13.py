"""Solution for day 13.

Part 1:
Find the number whose next multiple is closest to the first number and greater.

Part 2:
Compute the first number such that number + index mod input[index] = 0 for 
all other numbers of the input.
"""
import re
from copy import deepcopy
from typing import List


def parse_input_1() -> List[int]:
    """Parse the input for day 13.

    In part 1 'x' is omitted
    Returns
    -------
    List[int]
        list containing the input numbers
    """
    with open("./data/day_13.txt", "r") as f:
        lines = [int(n) for line in f for n in line.split(",") if re.match("^\d+", n)]
    return lines


def parse_input_2() -> List[int]:
    """Parse the input for day 13.

    In part 2 the first number is omitted, an 'x' is translated to 1.

    Returns
    -------
    List[int]
        list containing the input numbers
    """
    with open("./data/day_13.txt", "r") as f:
        lines = [
            int(n) if re.match("^\d+", n) else 1 for line in f for n in line.split(",")
        ]
    return lines[1:]


def part_one(l: List[int]) -> int:
    """Execute part 1.

    Parameters
    ----------
    l : List[int]
        input

    Returns
    -------
    int
        result
    """
    time = l[0]
    wait_times = [x - (time % x) for x in l[1:]]
    wait_time = min(wait_times)
    bus_id = l[wait_times.index(wait_time) + 1]
    return bus_id * wait_time


def part_two(l: List[int]) -> int:
    """Execute part 2.

    Parameters
    ----------
    l : List[int]
        input

    Returns
    -------
    int
        result
    """
    time = l[0]
    incr = l[0]
    for i in range(len(l)):
        if l[i] == 1:
            continue
        while (time + i) % l[i] != 0:
            time += incr
            print(time)
        if i == len(l) - 1:
            break
        incr = max(incr, lcm(incr, l[i]))
    return time


def lcm(a: int, b: int) -> int:
    """Find the least common multiple of a and b

    Parameters
    ----------
    a : int
        a
    b : int
        b

    Returns
    -------
    int
        least common multiple of a and b
    """
    return (a * b) // gcd(a, b)


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b.

    Parameters
    ----------
    a : int
        a
    b : int
        b

    Returns
    -------
    int
        greatest common divisor of a and b
    """
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


if __name__ == "__main__":
    l_1 = parse_input_1()
    r_1 = part_one(l_1)
    print(f"Result part one: {r_1}")
    l_2 = parse_input_2()
    r_2 = part_two(l_2)
    print(f"Result part two: {r_2}")
