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
        lst_pattern, lst_s = [i for i in pattern], s.split(' ')

        if len(lst_pattern) != len(lst_s):
            return False

        res = {}

        for i in range(len(lst_pattern)):
            if lst_pattern[i] in res.keys() and res[lst_pattern[i]] != lst_s[i]:
                return False

            if lst_s[i] in res.values() and lst_pattern[i] not in res.keys():
                return False

            res[lst_pattern[i]] = lst_s[i]

        return True


"""

This is better understood through the example:
s = ['a', 'b', 'b', 'a'], t = ['dog', 'dog', 'dog', 'dog'], list(zip(s, t)) = [('a', 'dog'), ('b', 'dog'), ('b', 'dog'), ('a', 'dog')], set(zip(s, t) = {('b', 'dog'), ('a', 'dog')}
Zip basically act as a zipper when called upon two lists, making a new list of tuples of two elements, one from each list. 
Therefore you see 4 tuples in the newly zipped list and then if you call set upon it, there should only be unique elements left. 
The length of the zipped set is 2, but the length of set t is 1, since there's only one kind of word, 'dog', in it, therefore we know there's a mismatch somewhere.

Generalize it to the entire problem, only when the set of the words, patterns, and word-pattern tuple have the same length, meaning everything matches, a full match can be achieved. Otherwise it's false. 

"""


class Solution1:
    def wordPattern(self, pattern, str):
        s = pattern
        t = str.split()

        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)

