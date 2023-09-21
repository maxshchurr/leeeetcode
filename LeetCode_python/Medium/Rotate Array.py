"""

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""

# slow runtime
class Solution:
    def rotate(self, nums: list[int], k: int) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k != 0:
            nums.insert(0, nums.pop())
            k -= 1


class Solution1:
    def rotate(self, nums: list[int], k: int) -> list:
        """
        Do not return anything, modify nums in-place instead.
        """
        # will count the number of the steps that we have run through to rotate the list
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
