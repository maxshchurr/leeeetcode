"""

You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



Example 1:

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.

"""


# probably the best approach
class Solution:
    def maximum69Number(self, num: int) -> int:
        try:
            return int(str(num).replace('6', '9', 1))
        except:
            return num

# intuitive way ( the idea is similar with the 1st Solution,
# but I forgot that we can specify the quantity of elements to replace that's why I used index instead )
class Solution1:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        num_lst = list(num)

        try:
            index_6 = num.index('6')
        except:
            return int(num)

        num_lst[index_6] = '9'

        return int(''.join(num for num in num_lst))

# fck brain
class Solution2:
    def maximum69Number(self, num: int) -> int:
        num = str(num)
        res = ''

        if num.count('9') == len(num):
            return int(num)

        for pos in range(len(num)):
            if num[pos] == '9':
                res += num[pos]
            else:
                res += '9'
                res += num[pos+1::]

        return int(res)
