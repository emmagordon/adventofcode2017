#!/usr/bin/env python3.6

"""Day 3 - Part 1:

Each square on a 2D grid is allocated in a spiral pattern like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

Data must be carried back to square 1 (the location of the only access
port for this memory system) by programs that can only move up, down,
left, or right. They always take the shortest path. For example:

>>> steps_to_access_port_from(1)
0
>>> steps_to_access_port_from(12)
3
>>> steps_to_access_port_from(23)
2
>>> steps_to_access_port_from(1024)
31

Part 2:

As a stress test on the system, the programs clear the grid and store the
value 1 in square 1. Then, in the same allocation order as shown above,
they store the sum of the values in all adjacent squares WRITTEN SO FAR,
including diagonals. Once a square is written, its value does not change,
so the grid is like so:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...

>>> stress_test_first_value_over(1)
2
>>> stress_test_first_value_over(6)
10
>>> stress_test_first_value_over(362)
747
"""

import itertools

PUZZLE_INPUT = 325489
RIGHT, UP, LEFT, DOWN = 1, 1j, -1, -1j
ACCESS_PORT = 0 + 0j


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


def manhattan_distance(point1, point2):
    return abs(point1.real - point2.real) + abs(point1.imag - point2.imag)


def steps_to_access_port_from(number):
    return int(manhattan_distance(location_on_spiral(number), ACCESS_PORT))


def stress_test_first_value_over(number):
    location, value = ACCESS_PORT, 1
    spiral_step = generate_spiral()
    values_by_location = {}

    while value <= number:
        values_by_location[location] = value
        location += next(spiral_step)
        value = sum(values_by_location.get(point, 0)
                    for point in adjacent_points(location))
    return value


def adjacent_points(point):
    return [(point + x + y) for x in [1, -1, 0] for y in [1j, -1j, 0]
            if not x == y == 0]

if __name__ == "__main__":
    print(steps_to_access_port_from(PUZZLE_INPUT))
    print(stress_test_first_value_over(PUZZLE_INPUT))
