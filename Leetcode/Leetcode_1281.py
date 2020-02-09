"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for i in str(n):
            product *= int(i)
            sum += int(i)

        print(product)
        print(sum)

        return product - sum

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.subtractProductAndSum(234))