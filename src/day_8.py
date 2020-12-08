"""Solution for day 7.

Part 1:
Execute the given code.

Part 2:
Count the amount of bags required to be inside a shiny gold bag.
"""
from copy import deepcopy
from typing import List, Tuple


def parse_input():
    """Parse the input of this problem."""
    with open("./data/day_8.txt", "r") as f:
        lines = [line.strip().split(" ") for line in f]
    return lines


def nop(
    lines: List[str], index: int, acc: int, visited: List[int]
) -> Tuple[List[str], int, int, List[int]]:
    """Execute a nop.

    Parameters
    ----------
    lines : List[str]
        list of commands to execute
    index : int
        pointer to command currently being executed
    acc : int
        accumulator of the commands being executed
    visited : List[int]
        list of indexes of commands already executed

    Returns
    -------
    Tuple[List[str], int, int, List[int]]
        tuple containing lines, index, acc and visited
    """
    index += 1
    return next_instruction(lines, index, acc, visited)


def acc(
    lines: List[str], index: int, acc: int, visited: List[int]
) -> Tuple[List[str], int, int, List[int]]:
    """Execute an acc.

    Parameters
    ----------
    lines : List[str]
        list of commands to execute
    index : int
        pointer to command currently being executed
    acc : int
        accumulator of the commands being executed
    visited : List[int]
        list of indexes of commands already executed

    Returns
    -------
    Tuple[List[str], int, int, List[int]]
        tuple containing lines, index, acc and visited
    """
    acc += int(lines[index][1])
    index += 1
    return next_instruction(lines, index, acc, visited)


def jmp(
    lines: List[str], index: int, acc: int, visited: List[int]
) -> Tuple[List[str], int, int, List[int]]:
    """Execute a jmp.

    Parameters
    ----------
    lines : List[str]
        list of commands to execute
    index : int
        pointer to command currently being executed
    acc : int
        accumulator of the commands being executed
    visited : List[int]
        list of indexes of commands already executed

    Returns
    -------
    Tuple[List[str], int, int, List[int]]
        tuple containing lines, index, acc and visited
    """
    index += int(lines[index][1])
    return next_instruction(lines, index, acc, visited)


def next_instruction(
    lines: List[str], index: int, acc: int, visited: List[int]
) -> Tuple[List[str], int, int, List[int]]:
    """Execute the next instruction if the program shouldn't be terminated.

    The program should be terminated if a command is about to be executed for the second time or the last command was executed.

    Parameters
    ----------
    lines : List[str]
        list of commands to execute
    index : int
        pointer to command currently being executed
    acc : int
        accumulator of the commands being executed
    visited : List[int]
        list of indexes of commands already executed

    Returns
    -------
    Tuple[List[str], int, int, List[int]]
        tuple containing lines, index, acc and visited
    """
    if index == len(lines):
        return lines, index, acc, visited

    if index in range(len(lines)) and not index in visited:
        visited.append(index)
        return globals()[lines[index][0]](lines, index, acc, visited)
    if index in visited:
        return lines, index, acc, visited


def part_one():
    """Execute part 1."""
    lines = parse_input()
    l, i, a, v = next_instruction(lines, 0, 0, [])
    print("Failed", f"Index: {i}", f"Accumulator: {a}", sep="\n")


def part_two():
    """Execute part 2."""
    lines = parse_input()
    for x in range(len(lines)):
        if lines[x][0] == "nop" or lines[x][0] == "jmp":
            temp_lines = deepcopy(lines)
            temp_lines[x][0] = "nop" if temp_lines[x][0] == "jmp" else "jmp"

            l, i, a, v = next_instruction(temp_lines, 0, 0, [])
            if i == len(l):
                print(
                    "Success",
                    f"Corrected commands: {l}",
                    f"Index: {i}",
                    f"Accumulator: {a}",
                    sep="\n",
                )
                break


if __name__ == "__main__":
    part_one()
    part_two()
