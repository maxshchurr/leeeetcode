"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
"""


# My solution - enormous runtime
class Solution:
    def singleNumber(self, nums: [int]):
        nums_set = set(nums)
        for i in nums_set:
            if nums.count(i) == 1:
                return i


"""

^	XOR	
Sets each bit to 1 if only one of two bits is 1
Any number XORed with itself is 0, so each duplicate number will "cancel out" itself, 
except for the number that only exists once in the list

"""


# Didn't know about this operator
class Solution1:
    def singleNumber1(self, nums: [int]):
        xor = 0
        for num in nums:
            xor ^= num

        return xor


# Another solution
class Solution2:
    def singleNumber2(self, nums):
        dic = {}
        for num in nums:
            # if the key is not found set value = 0 and then + 1
            dic[num] = dic.get(num, 0)+1
        for key, val in dic.items():
            if val == 1:
                return key
