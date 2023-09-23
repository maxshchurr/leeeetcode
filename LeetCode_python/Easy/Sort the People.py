"""

You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.



Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

"""


# this wont work as expected if there will be same heights in heights list, cause it is used as a key
# for our height_dict, which means that if we will find the same key (height), the previous will be erased
class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        # will store height (from heights) as a key and name (from names) as a value
        height_dict = dict(zip(heights, names))

        sorted_by_height = []
        for height in sorted(height_dict.keys(), reverse=True):
            sorted_by_height.append(height_dict[height])

        return sorted_by_height


# same idea
class Solution1:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        sorted_by_height = []
        heights_and_names = list(zip(heights, names))

        for height, name in sorted(heights_and_names, reverse=True):
            sorted_by_height.append(name)

        return sorted_by_height
