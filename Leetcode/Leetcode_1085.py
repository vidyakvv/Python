"""
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
Return 0 if S is odd, otherwise return 1.
Input: [99,77,33,66,55]
Output: 1
Explanation:
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
"""

from typing import List

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_num = min(A)
        sum_digits = 0
        min_num_str = str(min_num)
        print(min_num_str)
        for each_digit in min_num_str:
            sum_digits += int(each_digit)
        if sum_digits%2 == 0:
            return 1
        else:
            return 0
        """return 1 - sum([int(i) for i in str(min(A))]) % 2"""


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.sumOfDigits([99,77,33,66,55]))