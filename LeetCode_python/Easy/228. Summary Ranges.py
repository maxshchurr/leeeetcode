"""

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


"""


# yeap, it's disgusting
class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]

        res = []

        current_range = [nums[0]]

        for i in range(1, len(nums)):
            if current_range[-1] + 1 != nums[i]:
                if len(current_range) == 1:
                    res.append(str(current_range[0]))
                else:
                    res.append(f"{current_range[0]}->{current_range[-1]}")

                current_range = [nums[i]]

            else:
                current_range.append(nums[i])

            if i == len(nums) - 1:
                if len(current_range) == 1:
                    res.append(str(current_range[0]))
                else:
                    res.append(f"{current_range[0]}->{current_range[-1]}")

        return res


# seams nicer than previous one
class Solution1:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        start, end = 0, 0

        while start < len(nums) and end < len(nums):
            if (end + 1) < len(nums) and nums[end] + 1 == nums[end + 1]:
                end = end + 1

            else:
                if nums[start] == nums[end]:
                    result.append(str(nums[start]))
                    start = start + 1
                    end = end + 1
                else:
                    result.append(str(nums[start]) + '->' + str(nums[end]))
                    end = end + 1
                    start = end

        return result
