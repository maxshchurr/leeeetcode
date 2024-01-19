"""

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        self.helper(res, root, 0)

        return res

    def helper(self, res, root, d):
        if not root:
            return

        if d == len(res):
            res.append(root.val)

        else:
            res[d] = max(res[d], root.val)

        self.helper(res, root.left, d + 1)
        self.helper(res, root.right, d + 1)
