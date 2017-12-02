#!/usr/bin/env python3.6

"""The captcha requires you to review a sequence of digits and find the
sum of all digits that match the next digit in the list. The list is
circular, so the digit after the last digit is the first digit in the list.

For example:

>>> solve("1122")
3
>>> solve("1111")
4
>>> solve("1234")
0
>>> solve("91212129")
9
"""


def solve(captcha):
    next_digit_comparisons = zip(captcha, captcha[1:] + captcha[0])
    return sum([int(d) for d, d2 in next_digit_comparisons if d == d2])


if __name__ == "__main__":
    with open("captcha_input.txt", "r") as f:
        puzzle_input = f.read()

    print(solve(puzzle_input))
