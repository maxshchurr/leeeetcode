"""

Given an integer array nums, return the length of the longest strictly increasing
subsequence
.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

"""
import bisect


# a bit of cheating, because we don't store the corresponding list, but the task is to get its length
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = [nums.pop()]

        for i in nums:
            if i > res[-1]:
                res.append(i)
            else:
                # bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
                # Locate the insertion point for x in a to maintain sorted order.
                # The parameters lo and hi may be used to specify a subset of the list which should be considered;
                # by default the entire list is used.
                idx = bisect.bisect_left(res, i)
                res[idx] = i

        return len(res)


class Solution1:
    def lengthOfLIS(self, nums: list[int]) -> int:
        total_number = len(nums)
        dp = [0 for i in range(total_number)]

        for i in range(1, total_number):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp) + 1
