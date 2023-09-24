"""

There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.



Example 1:

Input: piles = [2,4,1,2,7,8]
Output: 9
Explanation: Choose the triplet (2, 7, 8), Alice Pick the pile with 8 coins, you the pile with 7 coins and Bob the last one.
Choose the triplet (1, 2, 4), Alice Pick the pile with 4 coins, you the pile with 2 coins and Bob the last one.
The maximum number of coins which you can have are: 7 + 2 = 9.
On the other hand if we choose this arrangement (1, 2, 8), (2, 4, 7) you only get 2 + 4 = 6 coins which is not optimal.
Example 2:

Input: piles = [2,4,5]
Output: 4
Example 3:

Input: piles = [9,8,7,6,5,1,2,3,4]
Output: 18

"""


class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles = sorted(piles, reverse=True)
        quan = len(piles) // 3
        you = []
        i = 1
        while quan > 0:
            you.append(piles[i])
            i += 2
            quan -= 1

        return sum(you)


# probably not very readable
class Solution1:
    def maxCoins(self, piles: list[int]) -> int:
        """
        Bob picks minimum coin each time, which means that if our array is sorted and we know how many coins each person will grab,
        we can start from the piles[i] where [i] will be len(piles)//3 -> quantity of coins that each person will grab;
        ::2 -> as 2 from 3 persons are left, we have to define the step = 2, because Alice picks max coin
        """
        return sum(sorted(piles)[len(piles) // 3::2])


# same idea as in Solution1 but more readable
class Solution2:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        coins = 0
        for x in range(len(piles) // 3, len(piles), 2):
            coins += piles[x]

        return coins
