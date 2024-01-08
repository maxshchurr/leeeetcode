"""

You are playing the following Nim Game with your friend:

Initially, there is a heap of stones on the table.
You and your friend will alternate taking turns, and you go first.
On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
The one who removes the last stone is the winner.
Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.



Example 1:

Input: n = 4
Output: false
Explanation: These are the possible outcomes:
1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
In all outcomes, your friend wins.
Example 2:

Input: n = 1
Output: true
Example 3:

Input: n = 2
Output: true

"""


"""
The technique here is simple, you are the first person to take the stones, as you know you can win when there are 1,2,3 stones left and lose when 4 stones are left. 
It is just forcing your opponent to bring the heap total to 4 at some point(your opponent should have to choose from 4 stones, which means he looses for sure). 
You can force to 4 remaining stones when the heap contains 4k+1, 4k+2, 4k+3 and not when 4x (where k = x+1). What you are given as an example is just a subgame and very helpful. To solve this question, you just need to understand this logic. Thus "return n%4" is the answer to the problem. 
This code implies return True when n%4 !=0 and False when n%4==0
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
