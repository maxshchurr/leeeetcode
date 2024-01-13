"""

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.

"""
from collections import Counter


# nice one line solution
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return (Counter(s)-Counter(t)).total()


class Solution1:
    def minSteps(self, s: str, t: str) -> int:
        s, t = Counter(s), Counter(t)
        ans = 0

        for c in s.keys():
            # if there is no such key in Counter(t) it will return 0 instead of the KeyException
            ans += s[c] - min(t[c], s[c])

        return ans


s = "leetcode"
t = "practice"
ttt = Counter(s)
print(ttt["a"])
print(Solution1().minSteps(s, t))