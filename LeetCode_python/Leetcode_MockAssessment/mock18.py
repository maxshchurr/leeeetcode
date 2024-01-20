"""



"""


from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        cnt_first = Counter(words[0])

        for word in range(1, len(words)):
            cnt = Counter(words[word])
            for k in cnt_first.keys():
                cnt_first[k] = min(cnt_first[k], cnt[k])

        res = []
        for k, freq in cnt_first.items():
            res.extend([k] * freq)
        # res = [k for k, freq in cnt_first.items() for _ in range(freq)] the same but in one line

        return res
