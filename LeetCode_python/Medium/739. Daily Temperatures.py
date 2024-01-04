"""

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = []

        for i in range(len(temperatures) - 1):
            cnt = 1

            if temperatures[i+1] > temperatures[i]:
                res.append(cnt)

            else:
                tmp = i
                while temperatures[tmp+1] <= temperatures[tmp]:
                    if tmp == len(temperatures)-1:
                        res.append(0)
                        break
                    cnt += 1
                    tmp += 1
                res.append(cnt)

        res.append(0)

        return res


temperatures = [73,74,75,71,69,72,76,73]

print(Solution().dailyTemperatures(temperatures))