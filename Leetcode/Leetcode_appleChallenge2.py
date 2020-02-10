"""

Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]


"""


############################### Need to be fixed ###################################
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1  # 5
        # target_index = -1 # target =8
        required_list = [-1, -1]

        while start < end:
            mid = (start + end) // 2  # 2
            print("start: "+str(start))
            print("end: "+str(end))
            print(mid)
            print("1111111111111")
            if nums[mid] == target:
                start = mid
                end = mid
                print("mid: "+str(mid))
                while start > 0 and end < len(nums) and (nums[start] == target or nums[end] == target):
                    print("#############")
                    print("start2: "+str(start))
                    print("end2: " + str(end))

                    if nums[start] == target and start > 0:
                        start -= 1
                    elif nums[end] == target and end < len(nums):
                        end += 1
                    else:
                        break
                    required_list = [start+1 , end-1]
                break
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid

        return required_list

my_solution = Solution()
print(my_solution.searchRange([5,8,8,8,8], 8))




