"""

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.

"""


# from Solution chapter
class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        N = len(matrix)
        for i in range(1, N):
            for j in range(N):
                matrix[i][j] += min(matrix[i - 1][k] for k in (j - 1, j, j + 1) if 0 <= k < N)

        return min(matrix[-1])
