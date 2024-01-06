"""

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_p = 0

        for fast_p in range(len(nums)):
            if nums[fast_p] != 0 and nums[slow_p] == 0:
                nums[slow_p], nums[fast_p] = nums[fast_p], nums[slow_p]

            # to find an indexes of zero values
            if nums[slow_p] != 0:
                slow_p += 1
