"""

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.



Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1


"""

from collections import Counter


# not optimal
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)

        return -1


# using Counter to store dictionary with keys as char and values as its frequency
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)

        for i in s:
            if cnt[i] == 1:
                return s.index(i)

        return -1
