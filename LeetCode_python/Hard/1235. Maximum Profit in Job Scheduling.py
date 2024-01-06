"""

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.



Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6

"""

# FROM Solutions section, was too hard for me)

from bisect import bisect_left


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        n = len(startTime)
        events = []
        for i in range(n):
            # 1 for start event
            # 0 for end event
            # We want end events to occur before start event for same time
            events.append((startTime[i], 1, i))
            events.append((endTime[i], 0, i))

        events.sort()

        maxProfit = [0] * n
        previousMax = 0

        for time, eventType, index in events:
            # If it is a start event, calculate its maximum profit, using previous maximum profit
            if eventType == 1:
                maxProfit[index] = previousMax + profit[index]
            # If it is an end, update previous maximum profit
            else:
                previousMax = max(maxProfit[index], previousMax)

        return previousMax


class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        dp = [[0, 0]]  # e     s     p     dp
        #  ––-–  ––-–  ––-–  ––––––––––––––––-–
        f = lambda x: dp[bisect_left(dp, [x + 1]) - 1][1]  # 3     1    20   [[0,0],[3,20]]
        #    5     2    20   [[0,0],[3,20],[5,20]]
        for e, s, p in sorted(zip(endTime, startTime, profit)):  # 6     4    70   [[0,0],[3,20],[5,20],[6,90]]
            #    9     6    60   [[0,0],[3,20],[5,20],[6,90],[9,150]]
            dp.append([e, max(f(e), p + f(s))])  # 10     3   100   [[0,0],[3,20],[5,20],[6,90],[9,150],[10,150]]
            #                                                             |
        return dp[-1][1]  # answer