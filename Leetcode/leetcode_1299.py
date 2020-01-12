"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
"""
from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        required_list = []
        for i in range(len(arr)):
            required_list.append(0)
        max_num = -1
        """for i in range(len(arr)-1, -1, -1):
            required_list[i] = max_num
            max_num = max(arr[i], max_num)"""
        for i in range(-1, -len(arr)-1, -1):
            required_list[i] = max_num
            max_num = max(arr[i], max_num)
        return required_list


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.replaceElements([17, 18, 5, 4, 6, 1]))