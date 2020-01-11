"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
"""

class Solution:
    def removeVowels(self, S: str) -> str:
        required_string=""
        for letter in S:
            if letter in "aeiou":
                continue
            else:
                required_string = required_string+letter
        return required_string



if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.removeVowels("Leetcode"))