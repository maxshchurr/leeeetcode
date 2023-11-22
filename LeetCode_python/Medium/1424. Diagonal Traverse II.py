"""

Given a 2D integer array nums, return all elements of nums in diagonal order as shown in the below images.

Example 1:

Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]

Example 2:

Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

"""
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        """
        The purpose of defaultdict here is to append values to the list associated with a key without explicitly checking if the key exists
        Referring to a key which doesn't exist in dict will cause KeyError

        Key is the diagonal, values - nums in that diagonal
        """

        d = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])

        return [v for k in d.keys() for v in reversed(d[k])]
