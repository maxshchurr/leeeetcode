class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


# Faster than Solution
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        set_ransomNote = set(ransomNote)
        for i in set_ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True