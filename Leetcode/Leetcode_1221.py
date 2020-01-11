"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of split balanced strings.

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_splits =0
        count_letter = 0
        for letter in s:
            if letter == 'R':
                count_letter += 1

            if letter == 'L':
                count_letter -= 1

            if count_letter==0:
                num_splits += 1


        return num_splits


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.balancedStringSplit("RLRRLLRLRL"))