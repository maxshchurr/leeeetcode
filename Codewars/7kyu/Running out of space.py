"""

Kevin is noticing his space run out! Write a function that removes the spaces from the values and returns an array showing the space decreasing.
For example, running this function on the array ['i', 'have','no','space'] would produce ['i','ihave','ihaveno','ihavenospace']

"""


def spacey(array):
    tmp = ''
    res = []
    for i in array:
        tmp += i
        res.append(tmp)
    return res


def spacey(array):
    return [''.join(array[:i+1]) for i in range(len(array))]


from itertools import accumulate


def spacey(a):
    return list(accumulate(a))
