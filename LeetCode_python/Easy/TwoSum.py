"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""

# My solution - approximately 1 second runtime
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        result = []
        for i in range(len(nums)):
            val_to_search = target - nums[i]
            if val_to_search in nums and nums.index(val_to_search) != i:
                result.append(i)
                result.append(nums.index(val_to_search))
                break

        return result

nums = [3, 2, 4]
target = 6
sol = Solution()
print(sol.twoSum(nums, target))


# Approximately 0.1 second runtime
class Solution1:
    def twoSum(self, nums: [int], target: int) -> [int]:
        prev = {}
        for i, v in enumerate(nums):
            remaining = target - nums[i]
            if remaining in prev:
                return [i, prev[remaining]]

            prev[v] = i

nums1 = [3, 2, 4]
target1 = 6
sol1 = Solution1()
print(sol1.twoSum(nums1, target1))