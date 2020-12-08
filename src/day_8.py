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
    index += 1
    return next_instruction(lines, index, acc, visited)


def acc(
    lines: List[str], index: int, acc: int, visited: List[int]
) -> Tuple[List[str], int, int, List[int]]:
    acc += int(lines[index][1])
    index += 1
    return next_instruction(lines, index, acc, visited)


def jmp(
    lines: List[str], index: int, acc: int, visited: List[int]
) -> Tuple[List[str], int, int, List[int]]:
    index += int(lines[index][1])
    return next_instruction(lines, index, acc, visited)


def next_instruction(
    lines: List[str], index: int, acc: int, visited: List[int]
) -> Tuple[List[str], int, int, List[int]]:
    if index == len(lines):
        print(
            "Success",
            f"Corrected commands: {lines}",
            f"Index: {index}",
            f"Accumulator: {acc}",
            sep="\n",
        )
        return True

    if index in range(len(lines)) and not index in visited:
        visited.append(index)
        return globals()[lines[index][0]](lines, index, acc, visited)
    if index in visited and PRINT:
        print("Failed", f"Index: {index}", f"Accumulator: {acc}", sep="\n")
        return None


def part_one():
    """Execute part 1."""
    lines = parse_input()
    PRINT = True
    next_instruction(lines, 0, 0, [])


def part_two():
    """Execute part 2."""
    lines = parse_input()
    PRINT = False
    for x in range(len(lines)):
        if lines[x][0] == "nop" or lines[x][0] == "jmp":
            temp_lines = deepcopy(lines)
            temp_lines[x][0] = "nop" if temp_lines[x][0] == "jmp" else "jmp"

            if next_instruction(temp_lines, 0, 0, []):
                break


if __name__ == "__main__":
    part_one()
    part_two()
