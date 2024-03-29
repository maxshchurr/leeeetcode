"""

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).index(s, 1) < len(s)


class Solution1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, int(len(s) / 2) + 1):
            if set(s.split(s[0:i])) == {''}:
                return True
        return False
