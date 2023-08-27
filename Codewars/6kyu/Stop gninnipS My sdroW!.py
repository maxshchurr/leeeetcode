"""

Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

"""


def spin_words(sentence):
    lst = sentence.split()

    for i, word in enumerate(lst):
        if len(word) >= 5:
            lst[i] = word[::-1]

    res = ' '.join(word for word in lst)
    return res


# tried this type of solution but mistakenly put if else at the end of the expression like this:
# return ' '.join(word for word in sentence.split() if len(word) >= 5 else word[::-1])
def spin_words2(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())

