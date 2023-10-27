class Solution:
    def romanToInt(self, s):
        rule = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0

        # we don't include the last element because we check if rule[s[i]] value is less than rule[s[i+1]] value
        for i in range(len(s) - 1):
            if rule[s[i]] < rule[s[i + 1]]:
                result -= rule[s[i]]
            else:
                result += rule[s[i]]

        # because we didn't include last element of the s string
        return result + rule[s[-1]]
