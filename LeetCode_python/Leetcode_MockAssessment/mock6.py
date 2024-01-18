"""

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.



Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1

"""


from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        tiles = list(tiles)
        sequences = set()

        for i in range(1, n + 1):
            sequences.update(permutations(tiles, i))

        return len(sequences)


class Solution1:
    def numTilePossibilities(self, tiles: str) -> int:
        ds = []
        self.ans = set()
        self.solve(tiles, ds)
        return len(self.ans)

    def solve(self, tiles, ds):
        for i in range(len(tiles)):
            ds.append(tiles[i])
            self.ans.add("".join(ds[:]))
            self.solve(tiles[:i] + tiles[i + 1:], ds)
            ds.pop()

        return
