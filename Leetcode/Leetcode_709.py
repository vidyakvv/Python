"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Input: "Hello"
Output: "hello"
"""
"""
class Solution:
    def toLowerCase(self, str: str) -> str:
        required_str = ""
        for letter in str:
            if ord(letter) >= ord('A') and ord(letter) <= ord('Z'):
                required_str += chr(ord(letter)+32)
            else:
                required_str += letter
        return required_str


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.toLowerCase("HHello"))
"""
######################################## 1 Liner ##################################


class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join(chr(ord(letter)+32)if ord('Z') >= ord(letter) >= ord('A') else letter for letter in str)


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.toLowerCase("HHello"))