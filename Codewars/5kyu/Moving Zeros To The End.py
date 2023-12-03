"""

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]


"""


def move_zeros(lst):
    res = [i for i in lst if i != 0]
    res.extend([0] * lst.count(0))

    return res


def move_zeros(array):
    # because False < True -> we will sort elements that are != 0, then add all zeros to the end
    return sorted(array, key=lambda x: x == 0)
