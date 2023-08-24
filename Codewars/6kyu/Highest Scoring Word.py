"""

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.

"""


# one line solution))
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


def high2(x):
    x_lst = x.split()
    word_and_score = {}
    max_word = ''

    for word in x_lst:
        max_score = max(word_and_score.values()) if len(word_and_score) != 0 else 0
        word_and_score[word] = sum(ord(w)-96 for w in word)
        max_word = word if word_and_score[word] > max_score else max_word

    return max_word


# similar idea as for high2 function but probably cleaner
def high3(x):
    words = x.split()
    lst = []

    for word in words:
        scores = [sum([ord(char) - 96 for char in word])]
        lst.append(scores)

    return words[lst.index(max(lst))]
