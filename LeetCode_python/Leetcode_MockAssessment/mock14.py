"""

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

"""


from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        cnt_chars = Counter(chars)
        res = 0

        for w in words:
            cnt_w = Counter(w)
            if all(cnt_chars[c] >= v for c, v in cnt_w.items()):
                res += len(w)

        return res


class Solution1:
    def countCharacters(self, words: list[str], chars: str) -> int:
        cnt_chars = Counter(chars)
        ans = 0

        for word in words:
            word_count = Counter(word)

            good = True
            for c, freq in word_count.items():
                if cnt_chars[c] < freq:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans
