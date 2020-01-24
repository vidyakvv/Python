"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
also in sorted non-decreasing order.".
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        my_list =  [x ** 2 for x in A]
        my_list.sort()
        return my_list

    """
    return sorted(x ** 2 for x in A)
    """

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.sortedSquares([-4,-1,0,3,10]))