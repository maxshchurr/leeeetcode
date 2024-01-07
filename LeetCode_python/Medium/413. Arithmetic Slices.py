"""

An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.
Example 2:

Input: nums = [1]
Output: 0


"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        res = 0
        curr_sequence = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr_sequence += 1
                res += curr_sequence
            else:
                curr_sequence = 0

        return res


class Solution1:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        res = 0
        for i in range(2, len(nums)):
            j = i
            while j < len(nums):
                if nums[j] - nums[j - 1] == nums[j - 1] - nums[j - 2]:
                    res += 1
                    j += 1
                else:
                    break
        return res
