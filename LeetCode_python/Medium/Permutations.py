"""

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""
from itertools import permutations


# he-he, it's worth to know such solution
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return permutations(nums)


# searched that it is called backtracking task - will do this later
class Solution1:
    def permute(self, nums: list[int]) -> list[list[int]]:
        pass



