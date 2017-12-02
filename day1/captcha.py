#!/usr/bin/env python3.6

"""Day 1 - Part 1:

The captcha requires you to review a sequence of digits and find the
sum of all digits that match the next digit in the list. The list is
circular, so the digit after the last digit is the first digit in the
list. For example:

>>> solve("1122")
3
>>> solve("1111")
4
>>> solve("1234")
0
>>> solve("91212129")
9

Part 2:

Instead of considering the next digit, consider the digit halfway around
the circular list. The list has an even number of elements. For example:

>>> solve("1212", part2=True)
6
>>> solve("1221", part2=True)
0
>>> solve("123425", part2=True)
4
>>> solve("123123", part2=True)
12
>>> solve("12131415", part2=True)
4
"""


def solve(captcha, part2=False):
    i = int(len(captcha) / 2) if part2 else 1
    next_digit_comparisons = zip(captcha, captcha[i:] + captcha[:i])
    return sum([int(d) for d, d2 in next_digit_comparisons if d == d2])


if __name__ == "__main__":
    with open("captcha_input.txt", "r") as f:
        puzzle_input = f.read()

    print(solve(puzzle_input))
    print(solve(puzzle_input, part2=True))
