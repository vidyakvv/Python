"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Input: [2,2,1]
Output: 1
"""
from typing import List
class Solution :
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
        """
        a = 0
        for i in nums:
            a ^= i
        return a
        """



my_solution = Solution()
print(my_solution.singleNumber([2,2,3]))