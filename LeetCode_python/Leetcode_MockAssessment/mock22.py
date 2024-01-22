"""

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.


Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false

"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        tmp = [i for i in s]

        for i in range(len(s)):
            tmp.append(s[i])
            tmp.pop(0)

            if ''.join(i for i in tmp) == goal:
                return True

        return False


# from solutions chapter
class Solution1:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s + s
