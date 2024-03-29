"""

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

"""


from typing import List
from sys import maxsize


# sliding window approach
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = maxsize
        left, total = 0, 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res = min(res, i - left + 1)
                total -= nums[left]
                left += 1

        # if res == maxsize it means that there is no subarray whose sum is greater than or equal to target
        return res if res != maxsize else 0
