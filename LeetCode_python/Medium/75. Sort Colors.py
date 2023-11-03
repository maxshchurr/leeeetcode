"""

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]

"""


# using library's sort method
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a.sort()


class Solution1:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count0s = 0
        count1s = 0
        count2s = 0
        for idx in range(len(nums)):
            if nums[idx] == 0:
                count0s += 1
            elif nums[idx] == 1:
                count1s += 1
            elif nums[idx] == 2:
                count2s += 1

        idx = 0
        while count0s != 0:
            nums[idx] = 0
            idx += 1
            count0s -= 1

        while count1s != 0:
            nums[idx] = 1
            idx += 1
            count1s -= 1

        while count2s != 0:
            nums[idx] = 2
            idx += 1
            count2s -= 1


a = [1, 6, 2, 5, 3]
a.sort()

print(a)