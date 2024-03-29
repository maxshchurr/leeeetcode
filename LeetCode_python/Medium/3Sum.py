"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        negative_nums, positive_nums, zero_nums = [], [], []
        for num in nums:
            if num > 0:
                positive_nums.append(num)
            elif num < 0:
                negative_nums.append(num)
            else:
                zero_nums.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(negative_nums), set(positive_nums)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if zero_nums:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0)
        if len(zero_nums) >= 3:
            res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(negative_nums)):
            for j in range(i + 1, len(negative_nums)):
                target = -1 * (negative_nums[i] + negative_nums[j])
                if target in P:
                    res.add(tuple(sorted([negative_nums[i], negative_nums[j], target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(positive_nums)):
            for j in range(i + 1, len(positive_nums)):
                target = -1 * (positive_nums[i] + positive_nums[j])
                if target in N:
                    res.add(tuple(sorted([positive_nums[i], positive_nums[j], target])))

        return res
