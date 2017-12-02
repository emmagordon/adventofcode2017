#!/usr/bin/env python3.6

"""Day 2 - Part 1:

Calculate the spreadsheet's checksum. For each row, determine the
difference between the largest value and the smallest value; the
checksum is the sum of all of these differences. For example:

>>> calculate_checksum([[5, 1, 9, 5],
...                     [7, 5, 3],
...                     [2, 4, 6, 8]])
18

Part 2:

Find the only two numbers in each row where one evenly divides the
other - divide them, and add up each line's result. For example:

>>> sum_evenly_divisible_values([[5, 9, 2, 8],
...                              [9, 4, 7, 3],
...                              [3, 8, 6, 5]])
9
"""


def parse_spreadsheet(data):
    rows = data.splitlines()
    return [list(map(int, r.split())) for r in rows]


def calculate_checksum(spreadsheet):
    return sum([max(row) - min(row) for row in spreadsheet])


def sum_evenly_divisible_values(spreadsheet):
    division_results = []
    for row in spreadsheet:
        division_results.extend(int(x / y) for x in row for y in row
                                if (x % y == 0) and (x != y))
    return sum(division_results)

if __name__ == "__main__":
    with open("puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    spreadsheet_data = parse_spreadsheet(puzzle_input)

    print(calculate_checksum(spreadsheet_data))
    print(sum_evenly_divisible_values(spreadsheet_data))
