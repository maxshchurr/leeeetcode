"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
"""


# Bad solution
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        s_lst = s.split(" ")
        cnt = 0
        for i in s.split:
            if cnt == len(s_lst) - 1:
                result += i[::-1]
            else:
                result += i[::-1] + ' '
            cnt += 1

        return result


class Solution1:
    def reverseWords1(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])