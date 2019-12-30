""" Given an array nums of integers, return how many of them contain an even number of digits.


Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits. """

from typing import List
class Solution:
    def findNumbers(self, nums : List[int]) -> int:
        return sum(len(str(number)) % 2 == 0 for number in nums)


if __name__ == "__main__":

    my_solution = Solution()
    print(my_solution.findNumbers([12, 345, 2, 6, 7896]))
    #print(sum([1,1,2,3]))











