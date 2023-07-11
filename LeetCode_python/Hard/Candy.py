"""

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.


Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

"""


class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)

        # from right side to left
        for i in range(len(candies) - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candies[i + 1] >= candies[i]:
                candies[i] = candies[i + 1] + 1

        # from left side to recheck
        for i in range(1, len(candies)):
            if ratings[i - 1] < ratings[i] and candies[i - 1] >= candies[i]:
                candies[i] = candies[i - 1] + 1

        return sum(candies)


s = Solution()
arr = [1, 2, 2, 0, 3, 2, 1, 1]
print(s.candy(arr))