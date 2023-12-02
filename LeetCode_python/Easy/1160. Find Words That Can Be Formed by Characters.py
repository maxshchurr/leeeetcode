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
        cnt = 0
        cnt_chars = Counter(chars)

        for word in words:
            temp_cnt_chars = cnt_chars.copy()
            can_form_word = True

            for c in word:
                if temp_cnt_chars[c] <= 0:
                    can_form_word = False
                    break

                temp_cnt_chars[c] -= 1

            if can_form_word:
                cnt += len(word)

        return cnt
