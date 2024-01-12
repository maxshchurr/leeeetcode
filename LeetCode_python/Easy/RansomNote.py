"""

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


# Faster than Solution
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        set_ransomNote = set(ransomNote)
        for i in set_ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


class Solution3:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_cnt = Counter(magazine)

        for i in ransomNote:
            if i not in m_cnt or m_cnt[i] == 0:
                return False

            m_cnt[i] -= 1

        return True
