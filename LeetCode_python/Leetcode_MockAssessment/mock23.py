"""

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]

"""


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        res = []
        nums_set = set(nums)

        for i in nums_set:
            if nums.count(i) > len(nums) / 3:
                res.append(i)

        return res


class Solution1:
    def majorityElement(self, nums: list[int]) -> list[int]:
        nums_set = set(nums)
        return [i for i in nums_set if nums.count(i) > len(nums) / 3]
