"""

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

"""


def is_isogram(string):
    string = string.lower()
    string_set = set(string)
    for i in string_set:
        if string.count(i) > 1:
            return False

    return True


# modified is_isogram def solution
def is_isogram2(string):
    string_set = set(string.lower())

    return len(string_set) == len(string)


# one-line solution
def is_isogram3(string):
    return len(string) == len(set(string.lower()))
