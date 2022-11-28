"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
"""


# Brutal force
class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ""
        for i in address:
            if i == ".":
                result += f"[.]"
            else:
                result += i
        return result


# With replace method
class Solution1:
    def defangIPaddr1(self, address: str) -> str:
        return address.replace(".", "[.]")


# With join
class Solution2:
    def defangIPaddr2(self, address: str) -> str:
        return ''.join(i if i != '.' else '[.]' for i in address)