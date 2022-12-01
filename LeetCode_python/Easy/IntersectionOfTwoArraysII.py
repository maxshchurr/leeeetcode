"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
"""


from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        # So Counter(nums2) is actually a dictionary where key is a letter and value is quantity of this letter in the list
        nums2_cnt = Counter(nums2)
        result = []

        for i in nums1:
            if i in nums2_cnt and nums2_cnt[i] > 0:
                result.append(i)
                nums2_cnt[i] -= 1

        return result