input_lst = [1, 2, 2, 3, 1, 8, 3, 5, 8]

# simple approach
def find_unique_element(arr):
    for elem in arr:
        if arr.count(elem) == 1:
            return elem


"""
approach using xor operator (^)
XOR is a bitwise operator that is also known as Exclusive OR. 
It is a logical operator which outputs 1 when either of the operands is 1 (one is 1 and the other one is 0), but both are not 1, and both are not 0. 
In this example it will help us in such way:
We know that only one element is unique, and other elements appear 2 times.
If 2 same numbers will be used with the xor operator, result will be 0
For instance: 2 in binary -> 010
              2 in binary -> 010
                             000
This means that we can sum all numbers, same will sum up to 0 and only unique number will be left.
"""


def find_unique_element1(arr):
    unique = 0
    for i in arr:
        unique ^= i
    return unique
