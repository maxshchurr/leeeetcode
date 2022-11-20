"""

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution:
    """
    Каждый следующий шаг это сумма двух предыдущих:4 шаг = 3 + 2
                                                   5 шаг = 5 + 3
                                                   6 шаг = 8 + 5
    """
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        a = 3
        b = 2

        while n-3 > 0:
            a = a + b
            b = a - b
            n -= 1

        return a