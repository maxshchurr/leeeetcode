"""

You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:

items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.

Note: ret should be returned in ascending order by value.



Example 1:

Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
Output: [[1,6],[3,9],[4,5]]
Explanation:
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 5, total weight = 1 + 5 = 6.
The item with value = 3 occurs in items1 with weight = 8 and in items2 with weight = 1, total weight = 8 + 1 = 9.
The item with value = 4 occurs in items1 with weight = 5, total weight = 5.
Therefore, we return [[1,6],[3,9],[4,5]].
Example 2:

Input: items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
Output: [[1,4],[2,4],[3,4]]
Explanation:
The item with value = 1 occurs in items1 with weight = 1 and in items2 with weight = 3, total weight = 1 + 3 = 4.
The item with value = 2 occurs in items1 with weight = 3 and in items2 with weight = 1, total weight = 3 + 1 = 4.
The item with value = 3 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
Therefore, we return [[1,4],[2,4],[3,4]].
Example 3:

Input: items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
Output: [[1,7],[2,4],[7,1]]
Explanation:
The item with value = 1 occurs in items1 with weight = 3 and in items2 with weight = 4, total weight = 3 + 4 = 7.
The item with value = 2 occurs in items1 with weight = 2 and in items2 with weight = 2, total weight = 2 + 2 = 4.
The item with value = 7 occurs in items2 with weight = 1, total weight = 1.
Therefore, we return [[1,7],[2,4],[7,1]].


"""
from collections import Counter


# didn't know that we can use Counter to accumulate the weights of items with same value
class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        cnt = Counter(dict(items1))
        cnt += Counter(dict(items2))

        return sorted(cnt.items())


# works but doesn't pass all test cases because exceed time limit
class Solution1:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        res = [item for item in items1]
        res_items = [item[0] for item in res]

        to_add = []
        added_items = []

        for item in items2:
            for i in range(len(res)):
                if item[0] == res[i][0]:
                    res[i][1] += item[1]
                if item[0] not in res_items and item[0] not in added_items:
                    to_add += [[item[0], item[1]]]
                    added_items.append(item[0])

        res.extend(to_add)

        return sorted(res)


class Solution2:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        quantities = {}

        for item in items1:
            key, value = item[0], item[1]
            quantities[key] = quantities.get(key, 0) + value

        for item in items2:
            key, value = item[0], item[1]
            quantities[key] = quantities.get(key, 0) + value

        merged_items = [[key, value] for key, value in quantities.items()]

        return sorted(merged_items)
