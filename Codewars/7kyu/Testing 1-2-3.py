"""

Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

"""


def number(lines):
    for i in range(len(lines)):
        lines[i] = f'{i+1}: {lines[i]}'

    return lines


def number2(lines):
    return [f'{i}: {val}' for i, val in enumerate(lines, 1)]
