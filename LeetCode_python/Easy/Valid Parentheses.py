"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for char in s:
            if char in brackets.keys():
                stack.append(char)
            elif char in brackets.values():
                if len(stack) == 0:
                    return False
                elif brackets[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0


# the same idea but more readable
class Solution2:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for bracket in s:
            # running threw the brackets.keys()
            if bracket in brackets:
                stack.append(bracket)
            # running threw the brackets.values()
            elif len(stack) == 0 or brackets[stack.pop()] != bracket:
                return False
        return len(stack) == 0
