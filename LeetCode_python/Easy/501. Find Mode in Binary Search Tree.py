"""

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]

"""

from collections import Counter
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        nodes = []

        def preorder_traversal(root):
            if not root: return

            nodes.append(root.val)
            preorder_traversal(root.left)
            preorder_traversal(root.right)

        preorder_traversal(root)
        nodes_frequency = Counter(nodes)
        max_frequency = max(nodes_frequency.values())

        res = [n for n in nodes_frequency if nodes_frequency[n] == max_frequency]

        return res
