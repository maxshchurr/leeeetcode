"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dct = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i, word in enumerate(words):
            if word not in dct.values() and pattern[i] not in dct.keys():
                dct[pattern[i]] = word

        for i, p in enumerate(pattern):
            if p not in dct.keys() or dct[p] != words[i]:
                return False

        return True


"""

zip_longest - This iterator prints the values of iterables alternatively in sequence. 
If one of the iterables is printed fully, the remaining values are filled by the values assigned to fillvalue parameter.

For example:

x = [1, 2, 3, 4, 5, 6, 7]
y = [8, 9, 10]
z = list(zip_longest(x, y))
print(z)

Output:

[(1, 8), (2, 9), (3, 10), (4, None), (5, None), (6, None), (7, None)]

"""

from itertools import zip_longest


class Solution2:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern,s))))