"""
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where
indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

"""
from typing import List
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        oddcount=0
        my_list=[[0 for col in range(m)] for row in range(n)]
        print(my_list)

        for r,c in indices:
            for i in range(m):
                my_list[r][i] += 1
                print(my_list)
            for j in range(n):
                my_list[j][c] = my_list[j][c]+1
                print(my_list)
        print(my_list)

        for i in range(n):
            for j in range(m):
                if(my_list[i][j]%2==1):
                    oddcount += 1

        return oddcount

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.oddCells(2,2,[[1,1],[0,0]]))