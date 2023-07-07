"""

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

"""

from typing import List


# two pointers solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_pointer, r_pointer = 0, len(numbers) - 1

        while l_pointer < r_pointer:
            curr_sum = numbers[l_pointer] + numbers[r_pointer]
            if curr_sum < target:
                l_pointer += 1
            elif curr_sum > target:
                r_pointer -= 1
            else:
                # task counts indexes starting from 1 that's why we add +1 to both pointers
                return [l_pointer+1, r_pointer+1]


# using dictionary
class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dct = {}
        for i, num in enumerate(numbers):
            if target - num in dct:
                return [dct[target - num] + 1, i + 1]
            dct[num] = i


s = Solution2()
print(s.twoSum([2,7,11,15], 9))

