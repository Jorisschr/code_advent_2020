"""Solution for day 10.

Part 1:
Sort the input ascending add a 0 and max + 3.
Count the number of differences of 1 and 3 between each pair of succesive
numbers and multiply the results.

Part 2:
Find the number of valid configurations by leaving out numbers.
A configuration is valid if there is no gap larger than 3 between two
consecutive numbers.
"""
import operator
from collections import Counter
from functools import reduce
from itertools import combinations
from typing import List


def parse_input() -> List[int]:
    """Parse the input of this problem.

    Returns
    -------
    List[int]
        list containing 0, the input numbers sorted and the max input number + 3
    """
    with open("./data/day_10.txt", "r") as f:
        numbers = [int(line) for line in f]
    return [0] + sorted(numbers) + [max(numbers) + 3]


def part_one(l: List[int]) -> int:
    """Count the number of differences of 1 and 3, multiply the result

    Parameters
    ----------
    l : List[int]
        sorted list containing 0, the input numbers and max + 3

    Returns
    -------
    int
        product of the counts of 1, 3 in the differences of l
    """
    c = Counter(list(map(operator.sub, l[1:], l[:-1])))
    return c[1] * c[3]


def part_two(l: List[int]) -> int:
    """Calculate the number of valid configurations

    Parameters
    ----------
    l : List[int]
        sortd list containing 0, the input numbers and max + 3

    Returns
    -------
    int
        number of valid configurations
    """
    sequences = find_all_sequences(l)
    return reduce(operator.mul, [count_configs(sequence) for sequence in sequences])


def find_all_sequences(numbers: List[int]) -> List[List[int]]:
    """Find all sequences that have gaps of 3 with their neighbours.

    Parameters
    ----------
    numbers : List[int]
        sorted list containing 0, the input numbers and max + 3

    Returns
    -------
    List[List[int]]
        numbers divided into sequences with a gap of 3 or larger with their neighbours
    """
    sequences = []
    cur_seq = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] == 3:
            sequences.append(cur_seq)
            cur_seq = [numbers[i]]
        else:
            cur_seq.append(numbers[i])
    sequences.append(cur_seq)
    return sequences


def count_configs(sequence: List[int]) -> int:
    """Count the number of valid configurations for the given sequence

    Parameters
    ----------
    sequence : List[int]
        sorted sequence of numbers

    Returns
    -------
    int
        number of valid configurations
    """
    if len(sequence) > 2:
        sub_seq = sequence[1:-1]
        all_combinations = [
            [sequence[0]] + list(elem) + [sequence[-1]]
            for i in range(len(sub_seq) + 1)
            for elem in list(combinations(sub_seq, i))
        ]
        return sum(valid(c) for c in all_combinations)

    elif valid(sequence):
        return 1

    print("This should not happen...")
    return 0


def valid(numbers: List[int]) -> bool:
    """Check if a given list of numbers is valid

    Parameters
    ----------
    numbers : List[int]
        list of numbers to check

    Returns
    -------
    bool
        whether the list is valid
    """
    if len(numbers) == 1:
        return True
    return max(list(map(operator.sub, numbers[1:], numbers[:-1]))) <= 3


if __name__ == "__main__":
    l = parse_input()
    r_1 = part_one(l)
    print(f"Result part one: {r_1}")
    r_2 = part_two(l)
    print(f"Result part two: {r_2}")
