
"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S
and S < K. If no i, j exist satisfying this equation, return -1.

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation:
We can use 34 and 24 to sum 58 which is less than 60.
"""

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        ans = -1
        for j in range(-1, -len(A) - 1, -1):
            for i in range(j - 1, -len(A) - 1, -1):
                if A[i] + A[j] < K:
                    ans = max(ans, A[i] + A[j])
        return ans

        """ *** Ideal Solution **
        a = sorted(A) 
        i,j = 0,len(a)-1
        ans = -1
        while i<j:
            if a[i]+a[j]<K:
                ans = max(ans,a[i]+a[j])
                i += 1
            else:
                j -= 1
        return ans
        """