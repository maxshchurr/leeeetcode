"""

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

"""


from typing import List


# 2 pointers solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_pointer, r_pointer = 0, len(height) - 1
        max_area = 0
        while l_pointer < r_pointer:
            # a = min(height[l_pointer], height[r_pointer]) - getting height of containers walls
            a = min(height[l_pointer], height[r_pointer])
            # b = r_pointer - l_pointer - getting width of container
            b = (r_pointer - l_pointer)
            # curr_area = a * b - getting area of rectangle
            curr_area = a * b
            max_area = max(max_area, curr_area)

            if height[l_pointer] < height[r_pointer]:
                l_pointer += 1
            else:
                r_pointer -= 1

        return max_area
