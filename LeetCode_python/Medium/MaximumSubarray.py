"""
Given an integer array nums, find the subarray which has the largest sum and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
"""


# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums):

        max_till_now = max(nums)
        max_ending = 0

        for i in nums:
            max_ending += i
            if max_ending < 0:
                max_ending = 0
            elif max_till_now < max_ending:
                max_till_now = max_ending

        return max_till_now