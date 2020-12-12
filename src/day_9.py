"""Solution for day 9.

Part 1:
Find the first number in the list that is not a sum of 2 numbers in a preceding slice of 25.

Part 2:
Sum of the min and max number in the preceding slice of the invalid number

"""
from typing import List

def parse_input() -> List[int]:
    """Parse the input of this problem."""
    with open("./data/day_9.txt", "r") as f:
        numbers = [int(line.strip()) for line in f]
    return numbers


def part_one(to_consider: int) -> int:
    """Execute part 1.

    Parameters
    ----------
    to_consider : int
        length of the slice to use for validation

    Returns
    -------
    int
        first number that is not the result of a sum of two numbers in the preceding slice
    """
    numbers = parse_input()
    for i in range(to_consider, len(numbers)):
        found = False
        for j in range(i - to_consider, i):
            if found:
                break
            for m in range(j, i):
                if numbers[j] + numbers[m] == numbers[i]:
                    found = True
                    break
        if not found:
            print(numbers[i])
            return numbers[i]


def part_two(invalid_number) -> int:
    """Execute part 2."""
    numbers = parse_input()
    print(numbers.index(invalid_number))
    for i in range(numbers.index(invalid_number)):
        for j in range(i, numbers.index(invalid_number)):
            if (sum(numbers[i:j+1])) == invalid_number:
                print(i, j)
                s = numbers[i:j+1]
                print(max(s) + min(s))
                return i + j


if __name__ == "__main__":
    invalid_number = part_one(25)
    part_two(invalid_number)
