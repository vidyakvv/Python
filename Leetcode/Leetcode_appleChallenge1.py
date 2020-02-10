"""

Given an array of size n, find the majority element. T
he majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Input: [3,2,3]
Output: 3

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        majority_element = 0
        majority_count = 0
        for element in nums:
            if not element in dict:
                dict[element] = 1
            else:
                dict[element] += 1
            if dict[element] > majority_count:
                majority_count = dict[element]
                majority_element = element
        return majority_element

        """
        3 -> 2
        2 -> 1
        4 -> 1

        """
