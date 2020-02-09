"""
Given a string S and a character C, return an array of integers representing the shortest
distance from the character C in the string.
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

"""
from typing import List
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        first = 100000
        my_list = []
        next = S.find(C)
        for i in range(len(S)):
            my_list.append(min(abs(next-i), abs(first-i)))
            if next-i == 0:
                first = next
                next = first+S[i+1:].find(C)+1

        return my_list

if __name__ == "__main__":
    my_solution  = Solution()
    print(my_solution.shortestToChar("loveleetcode",'e'))