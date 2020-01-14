"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A,
followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""
from typing import List
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        for index in range(int((len(A)+1)/2)):
            if ((A[index] % 2) == 1) and ((A[~index] % 2) == 0):
                temp = A[index];
                A[index] = A[~index]
                A[~index] = temp
            elif ((A[index] % 2) == 1) and ((A[~index] % 2) == 1):
                temp = A.pop(index)
                A.append(temp)
            elif ((A[index] % 2) == 0) and ((A[~index] % 2) == 0):
                temp = A.pop(~index)
                A.insert(index+1,temp)
            else:
                continue
        return A
# maintain 2 index start and end
if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.sortArrayByParity([6,3,1,7,2,4]))
    # 6,4,3,1,7,2
    #