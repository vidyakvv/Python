"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

class Solution:
    def defangIPaddr(self, address: str) -> str:
        required_ip = address
        return(required_ip.replace(".","[.]"))

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.defangIPaddr("1.1.1.1"))