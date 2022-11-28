"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.
The values in the two lists should be returned in increasing order.

Note:

You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches will have the same outcome.


Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].
"""


# So this actually works, but exceeds time limit on 122/127 test case
class Solution:
    def findWinners(self, matches):
        winners = [player[0] for player in matches]
        loosers = [player[1] for player in matches]
        result = [[], []]

        for winner in set(winners):
            if winner not in set(loosers):
                result[0].append(winner)

        for player in loosers:
            if loosers.count(player) == 1:
                result[1].append(player)

        result = [sorted(result[0]), sorted(result[1])]
        return result


# Using hashmap
class Solution1:
    def findWinners1(self, matches):
        winners, losers, table = [], [], {}

        for winner, loser in matches:
            table[winner] = table.get(winner, 0)
            table[loser] = table.get(loser, 0) + 1

        for k, v in table.items():
            if v == 0:
                winners.append(k)
            if v == 1:
                losers.append(k)

        return [sorted(winners), sorted(losers)] # Problem asked to return sorted arrays.