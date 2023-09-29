"""

Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
some tests will include very large numbers.
test data only employs positive integers.


"""

"""
Possible approach (from stackoverflow)

Starting from the right, find the first digit that has at least one smaller digit to its right. We'll call that digit X.
Then find the largest digit that is to the right of X, and is smaller than X. We'll call that digit Y.
Swap X and Y. This makes the number smaller.
Then sort all of the digits to the right of Y in descending order. This makes the number as big as possible, without making it bigger than the original.
For example:

1262347  // original number
  ^  ^
  X  Y

1242367  // after the swap
  ^  ^
  Y  X

1247632  // after sorting digits to the right of Y
  ^
  Y 
"""


# well, I couldnt pass all test cases, so here is solution from Solutions chapter
def next_smaller(n):
    numbers = [int(i) for i in str(n)]

    for i in range(len(numbers) - 1, 0, -1):
    
        ## If a number is less than the number to its left, split into 2 lists
        if numbers[i] < numbers[i -1]:
            rearrange_list = numbers[i - 1:]  ## numbers on the right of i -1
            original_list = numbers[:i - 1]   ## numbers on the left of i -1
            less_than_values = []             ## will contain possible substitutions for i -1

            for i in rearrange_list:
                if i < rearrange_list[0]:
                    less_than_values.append(i)
    
            # Add the max value from less_than_values to the end of the original_list,
            # then add the rest of the sorted values from rearrange_list to the original_list
            original_list.append(max(less_than_values))
            rearrange_list.remove(max(less_than_values))
            original_list += sorted(rearrange_list, reverse=True)
            
            # Join the list together to get the output
            output = int(''.join([str(num) for num in original_list]))

            ## If the output starts with 0, return -1. Otherwise, return the ouput.
            if len(str(output)) < len(str(n)):
                return -1
            else:
                return output
    
    ## Return -1 if n is None, or if there are no smaller numbers
    return -1


print(next_smaller(194))