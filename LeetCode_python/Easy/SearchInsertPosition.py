"""
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""


# My solution
class Solution:
    def searchInsert(self, nums, target):
        if nums is None:
            return 0

        tmp = []
        if target not in nums:
            for value in nums:
                if value < target:
                    tmp.append(value)
                if value > target:
                    break
            return len(tmp)

        for position, value in enumerate(nums):
            if target == value:
                return position


# Using sorted method
class Solution1:
    def searchInsert1(self, nums, target):
            nums.append(target)
            return sorted(nums).index(target)