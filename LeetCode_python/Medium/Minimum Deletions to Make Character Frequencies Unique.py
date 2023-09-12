"""

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).

"""

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        # Counter store occurrences for each element and return dictionary with element as key and occurrences as value in an descending order of occurrence
        # this is helpful because we are asked for min elements to delete to make an unique amount of occurrences
        cnt = Counter(s) 
        frequencies = set()
        to_delete = 0
        
        # here we will iterate in an ascending order of occurrences
        for frequency in cnt.values():
            while frequency in frequencies and frequency > 0:
                frequency -= 1
                to_delete += 1
            
            frequencies.add(frequency)
            
        return to_delete
    