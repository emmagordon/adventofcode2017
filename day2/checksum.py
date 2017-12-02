#!/usr/bin/env python3.6


def parse_spreadsheet(data):
    rows = data.splitlines()
    return [list(map(int, r.split())) for r in rows]


def calculate_checksum(spreadsheet):
    return sum([max(row) - min(row) for row in spreadsheet])

if __name__ == "__main__":
    with open("puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    print(calculate_checksum(parse_spreadsheet(puzzle_input)))
