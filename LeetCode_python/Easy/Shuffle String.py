"""

You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.



Example 1:


Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
Example 2:

Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

"""


class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        dct = {}
        for i, c in zip(indices, s):
            dct[i] = c

        res = ''.join(dct[i] for i in range(len(dct)))

        return res



class Solution1:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = ""
        for i in range(len(indices)):
            res += s[indices.index(i)]

        return res


# almost the same as in Solution1, but using list to store chars
class Solution2:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [''] * len(s)
        for index, ch in enumerate(s):
            res[indices[index]] = ch

        return "".join(res)
