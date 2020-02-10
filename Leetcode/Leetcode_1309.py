""""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

"12#348926"
->not # return corresponding character
-> if # 3 characters including # prepend corresponding character

1) [] -> size 26  . Add all the alphabets. Manage # in program
2) Parse the input string (s) , in reverse order and return the required string

stack []
["6","2","9","8","4","3","12#"]
"abc" -> len = 3

"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        my_alphabets = []
        order = ord('a')

        for i in range(26):
            my_alphabets.append(chr(order))
            order += 1
        #print(my_alphabets)

        required_str = ""
        stack = []
        index = -1
        while index >= -(len(s)):
            if s[index] == '#':
                character_req = s[(index-2):index]
                index -= 3
            else:
                character_req = s[index]
                index -= 1
            #print(my_alphabets[int(character_req)-1])
            stack.append(my_alphabets[int(character_req)-1])

        while stack:
            required_str += stack.pop()

        return required_str


my_solution = Solution()
print(my_solution.freqAlphabets("10#11#12"))