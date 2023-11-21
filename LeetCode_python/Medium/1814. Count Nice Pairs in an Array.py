"""

You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4

"""

from collections import Counter


class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        tmp = [i - int(str(i)[::-1]) for i in nums]
        tmp_pairs = Counter(tmp)
        res = 0

        for n in tmp_pairs.values():
            """
            This helped me to understand how to count pairs
            
            The formula 𝑛(𝑛−1)/2for the number of pairs you can form from an 𝑛 element set has many derivations.

            One is to imagine a room with 𝑛 people, each of whom shakes hands with everyone else. 
            If you focus on just one person you see that he participates in 𝑛−1 handshakes. 
            Since there are 𝑛 people, that would lead to 𝑛(𝑛−1) handshakes.

            So the total of 𝑛(𝑛−1) counts every handshake twice, once for each of the two people involved. 
            So the number of handshakes is 𝑛(𝑛−1)/2
            """
            res += n * (n - 1) // 2

        return res % (10**9 + 7)
