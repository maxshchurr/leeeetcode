"""

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


"""

from collections import Counter


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = Counter(sentence)
        return len(letters) == 26


class Solution1:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence) < 26:
            return False

        letters = [chr(i) for i in range(97, 123)]
        for letter in sentence.lower():
            if letter in letters:
                letters.remove(letter)

        return len(letters) == 0


# similar idea as in Solution
class Solution2:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
