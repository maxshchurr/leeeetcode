"""

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]

        for i in range(numRows - 1):
            new_row = [1]
            for j in range(i):
                new_row.append(result[i][j] + result[i][j+1])
            new_row.append(1)
            result.append(new_row)

        return result


