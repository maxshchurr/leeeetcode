"""

Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.


Example 1:

Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
Output: [3,2]
Explanation: The values that are present in at least two arrays are:
- 3, in all three arrays.
- 2, in nums1 and nums2.
Example 2:

Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
Output: [2,3,1]
Explanation: The values that are present in at least two arrays are:
- 2, in nums2 and nums3.
- 3, in nums1 and nums2.
- 1, in nums1 and nums3.
Example 3:

Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
Output: []
Explanation: No value is present in at least two arrays.

"""


# brute force
class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        res = set()

        for n1 in nums1:
            if n1 in nums2 or n1 in nums3:
                res.add(n1)

        for n2 in nums2:
            if n2 in nums1 or n2 in nums3:
                res.add(n2)

        return list(res)

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3))
