"""

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.



Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']
        first_vowels = [vowel for vowel in s[0:len(s) // 2] if vowel in vowels]
        second_vowels = [vowel for vowel in s[len(s) // 2::] if vowel in vowels]

        return len(first_vowels) == len(second_vowels)


class Solution1:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        vowels = ['a', 'e', 'i', 'o', 'u']

        a_cnt, b_cnt = 0, 0
        for i in range(len(s)//2):
            if s[i] in vowels:
                a_cnt += 1
            if s[-i - 1] in vowels:
                b_cnt += 1

        return a_cnt == b_cnt
