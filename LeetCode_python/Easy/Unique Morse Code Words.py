"""

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.



Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
Example 2:

Input: words = ["a"]
Output: 1

"""


from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        moorse = {
            'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
            'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
            'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
            'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..'
        }

        arr = []
        for word in words:
            st = ''
            for w in word:
                st += moorse.get(w)
            arr.append(st)

        return len(set(arr))


class Solution2:

    MORSE = {
            'a': '.-',   'b': '-...', 'c': '-.-.', 'd': '-..',  'e': '.',    'f': '..-.', 'g': '--.',
            'h': '....', 'i': '..',   'j': '.---', 'k': '-.-',  'l': '.-..', 'm': '--',   'n': '-.',
            'o': '---',  'p': '.--.', 'q': '--.-', 'r': '.-.',  's': '...',  't': '-',    'u': '..-',
            'v': '...-', 'w': '.--',  'x': '-..-', 'y': '-.--', 'z': '--..',
    }

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        return len(set(map(self.encode, words)))

    @classmethod
    def encode(cls, word: str) -> str:
        return ''.join(map(cls.MORSE.get, word))

