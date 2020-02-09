"""

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).
"""

class Solution:
    def fib(self, N :int) -> int:
        if N==0:
            return 0
        elif N==1:
            return 1
        else:
            fib_arr = [0] * (N+1) #N=4 [0,0,0,0,0]
            fib_arr[0] = 0
            fib_arr[1] = 1
            for i in range(2, N+1, 1):
                fib_arr[i] = fib_arr[i-1] + fib_arr[i-2]
            return fib_arr[N]


""" ** Complete recursive **

        if N == 0:
            return 0
        elif N == 1:
            return 1
        else :
            return self.fib(N-1) + self.fib(N-2)

"""




if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.fib(10))