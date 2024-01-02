"""

Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.



Example 1:

Input: num = "51230100"
Output: "512301"
Explanation: Integer "51230100" has 2 trailing zeros, we remove them and return integer "512301".
Example 2:

Input: num = "123"
Output: "123"
Explanation: Integer "123" has no trailing zeros, we return integer "123".

"""


# The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip('0')


class Solution1:
    def removeTrailingZeros(self, num: str) -> str:
        while num[-1] == '0':
            num = num[0:-1]

        return num