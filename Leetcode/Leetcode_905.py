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
        my_list = [0] * len(A)
        #print(my_list)
        start_index = 0
        end_index = len(A)-1
        for element in A:
            if element % 2 == 0 :
                my_list.remove(my_list[start_index])
                my_list.insert(start_index, element)
                start_index += 1
            else:
                my_list.remove(my_list[end_index])
                my_list.insert(end_index, element)
                end_index -= 1

        return my_list
"""
return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])
"""
if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.sortArrayByParity([6,3,1,7,2,4]))
    # 6,4,3,1,7,2
    #