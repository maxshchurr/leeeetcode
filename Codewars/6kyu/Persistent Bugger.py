"""

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)

"""


def persistence(n):
    n = str(n)
    cnt = 0
    tmp = 1

    while len(n) != 1:
        for digit in n:
            tmp *= int(digit)

        cnt += 1
        n, tmp = str(tmp), 1

    return cnt
