"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None: # length = 5
        left = 0
        right = len(s) - 1
        while left < right :
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        """
        for i in range(len(s)//2) :
            temp = s[i]
            s[i] = s[-1-i]
            s[-1-i] = temp
        """


if __name__ == "__main__":
    my_solution = Solution()
    my_list = ["h", "e", "l", "l", "o"]
    my_solution.reverseString(my_list)
    print(my_list)
