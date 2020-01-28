"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain,
return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Input: [0,1,0]
Output: 1
"""
from typing import List
class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:

        """********** Better in larger Arrays - Binary search ***************"""
        """ Doesn't work if there are repetition of numbers, eg: [0,1,1,1,1,1,1,12] """

        left, right = 0, len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid - 1] <= A[mid] and A[mid] <= A[mid + 1]:
                left = mid
            elif A[mid - 1] >= A[mid] and A[mid] >= A[mid + 1]:
                right = mid
            else:
                break
        return mid

        """Linear Search"""
        """for index in range(len(A)-1):
            if A[index] > A[index+1]:
                return index
                
        ******* 1 Liner Solution ************   
            return A.index(max(A))
        """

        """ Faster : beats 99% """
        """ lo, hi = 0, len(A)-1
            mid = lo + hi // 2
            if A[mid]<A[mid+1]:
                lo= mid+1
            else :
                hi = mid
            for index in range(lo , hi+1, 1):
                if A[index] > A[index+1]:
                    return index """



if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.peakIndexInMountainArray([0,0,1,2,2,2,2,2,3,3,8,3,3,3,2,1,0]))
