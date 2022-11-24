"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""


class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)

        return result


# Using set and & operator
class Solution1:
    def intersection1(self, nums1: [int], nums2: [int]) -> [int]:
        return list(set(nums1) & set(nums2))