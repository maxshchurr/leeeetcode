"""

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

"""


class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        min_values_in_row = {}
        for lst in matrix:
            min_val = min(lst)
            min_values_in_row[min_val] = lst.index(min_val)

        max_val = max(min_values_in_row)
        for lst in matrix:
            if max_val < lst[min_values_in_row[max_val]]:
                return []

        return [max_val]


# cool one line solution
class Solution1:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        return set(map(min, matrix)) & set(map(max, zip(*matrix)))
