"""

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]

"""


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        return [sum(nums) - sum(set(nums)), sum(range(1, len(nums))) - sum(set(nums))]


# intuitive approach
class Solution1:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        missed = occurs_twice = 0

        for i in range(1, len(nums)):
            if nums.count(nums[i]) == 2:
                occurs_twice = nums[i]

            if nums[i] not in nums:
                missed = nums[i]

            if missed and occurs_twice:
                return [occurs_twice, missed]
