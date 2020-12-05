"""Solution for day 5.

Part 1:
Parse seat numbers into integers then calculate the seat_id -> find the largest seat_id

Part 2:
Find your seat id. The plane is full so there is just 1 id missing from the list
"""
from typing import List


def parse_input() -> List[str]:
    """Parse the input of day 5.

    Returns
    -------
    List[str]
        list containing the lines of the input
    """
    with open("./data/day_5.txt", 'r') as f:
        lines = f.read().split("\n")
    return lines


def part_one() -> None:
    """Solve part 1."""
    lines = parse_input()
    s = "BFFFBBFRRR"
    s = "FFFBBBFRRR"
    s = "BBFFBBFRLL"

    largest_id = 0
    for s in lines:
        row = s[:7]
        column = s[7:]

        row_bits = row.replace("B", "1").replace("F", "0")
        column_bits = column.replace("R", "1").replace("L", "0")
        row_number = bits_to_int(row_bits)
        col_number = bits_to_int(column_bits)
        seat_id = get_seat_id(row_number, col_number)
        largest_id = seat_id if seat_id > largest_id else largest_id
    print(largest_id)


def part_two() -> None:
    """Solve part 2."""
    lines = parse_input()
    all_ids = []
    for s in lines:
        row = s[:7]
        column = s[7:]

        row_bits = row.replace("B", "1").replace("F", "0")
        column_bits = column.replace("R", "1").replace("L", "0")
        row_number = bits_to_int(row_bits)
        col_number = bits_to_int(column_bits)
        seat_id = get_seat_id(row_number, col_number)
        all_ids.append(seat_id)

    sorted_ids = sorted(all_ids)
    for x in range(len(sorted_ids) - 1):
        if sorted_ids[x + 1] - sorted_ids[x] == 2:
            print(sorted_ids[x] + 1)


def get_seat_id(row: int, column: int) -> int:
    """Calculate the seat id given the row and column number of a seat.

    Parameters
    ----------
    row : int
        row number
    column : int
        col number

    Returns
    -------
    int
        id of the seat
    """
    return row * 8 + column


def bits_to_int(bits) -> int:
    """Convert the given string of bits to int.

    Parameters
    ----------
    bits : str
        string representing bits (little endian)

    Returns
    -------
    int
        number represented by the given bitstring
    """
    x = 0
    bits = bits[::-1]
    for i in range(len(bits)):
        x += 2**i * int(bits[i])
    return x


if __name__ == "__main__":
    part_one()
    part_two()
