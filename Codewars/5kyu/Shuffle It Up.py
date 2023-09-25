"""

We have an array of unique elements. A special kind of permutation is the one that has all of its elements in a different position than the original.

Let's see how many of these permutations may be generated from an array of four elements. We put the original array with square brackets and the wanted permutations with parentheses.

arr = [1, 2, 3, 4]
      (2, 1, 4, 3)
      (2, 3, 4, 1)
      (2, 4, 1, 3)
      (3, 1, 4, 2)
      (3, 4, 1, 2)
      (3, 4, 2, 1)
      (4, 1, 2, 3)
      (4, 3, 1, 2)
      (4, 3, 2, 1)
      _____________
A total of 9 permutations with all their elements in different positions than arr

"""

from itertools import permutations
from math import factorial


# well, this solution works, but for big array_length it exceeds time limit, as the algorithm isnt efficient
def all_permuted(array_length):
    arr = [i for i in range(1, array_length+1)]
    all_permutations = list(permutations(arr))
    res = []

    for i in range(len(arr)):
        for permutation in all_permutations:
            if permutation[i] == arr[i]:
                res.append(permutation)

    final = [i for i in all_permutations if i not in res]
    return len(final)


"""
Thanks to Chat-GPT, he advised to use something called "derangement".
In combinatorial mathematics, a derangement is a permutation of the elements of a set in which no element appears in its original position.
D(n) = n! * (1 - 1/1! + 1/2! - 1/3! + 1/4! - 1/5! + ... + (-1)^n/n!) -> n is a number of elements, ! is a factorial

IDK why, it still exceeds time limit on Codewars, but passes 300+ test cases, so I can assume that it's efficient
"""


def all_permuted1(array_length):
    if array_length < 2:
        return 0

    total_permutations = factorial(array_length)
    derangements = 0

    for k in range(array_length + 1):
        derangements += (-1) ** k * (total_permutations // factorial(k))

    return derangements
