"""Given an integer n, return any array containing n unique integers such that they add up to 0.
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
"""
from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return list(range(1-n,n,2))

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.sumZero(8))