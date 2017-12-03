#!/usr/bin/env python3.6

"""For example:

>>> steps_to_access_port_from(1)
0
>>> steps_to_access_port_from(12)
3
>>> steps_to_access_port_from(23)
2
>>> steps_to_access_port_from(1024)
31
"""

import itertools

PUZZLE_INPUT = 325489
RIGHT, UP, LEFT, DOWN = 1, 1j, -1, -1j


def generate_spiral():
    directions = itertools.cycle([RIGHT, UP, LEFT, DOWN])
    step_size = 1
    while True:
        for _ in range(2):
            direction = next(directions)
            for _ in range(step_size):
                yield direction
        step_size += 1


def location_on_spiral(num):
    return sum(itertools.islice(generate_spiral(), num - 1))


def manhattan_distance_from_origin(point):
    return int(abs(point.real) + abs(point.imag))


def steps_to_access_port_from(number):
    return manhattan_distance_from_origin(location_on_spiral(number))

if __name__ == "__main__":
    print(steps_to_access_port_from(PUZZLE_INPUT))
