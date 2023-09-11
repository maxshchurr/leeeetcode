"""

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.



Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

"""

# a bit of cheating
class Solution:
    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i)[2:].count('1'))

        return res


# dynamic programming
class Solution1:
    """

    All whole numbers can be represented by 2N (even) and 2N+1 (odd).
    For a given binary number, multiplying by 2 is the same as adding a zero at the end (just as we just add a zero when multiplying by ten in base 10).
    Since multiplying by 2 just adds a zero, then any number and its double will have the same number of 1's.

    Likewise, doubling a number and adding one will increase the count by exactly 1. So:
    countBits(N) = countBits(2N)
    countBits(N)+1 = countBits(2N+1)
    Thus we can see that any number will have the same bit count as half that number, with an extra one if it's an odd number.

    i >> 1 is a bitwise operation and will be equal to i / 2 ** 1
    i << 1 will be equal to i * 2 ** 1

    """
    def countBits(self, n: int) -> list[int]:
        counter = [0]
        for i in range(1, n+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
