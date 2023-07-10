"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""


# non efficient
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for i in s:
            if s.count(i) != t.count(i):
                return False

        return True


# same idea as in Solution but set will make it much more effective with large long strings
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s, set_t = set(s), set(t)
        for i in set_s:
            if s.count(i) != t.count(i):
                return False

        return True
