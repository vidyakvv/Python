"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired
character. The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4.
"""

"""class Solution:
    def calculateTime(self, keyboard, word):
        total_time =0
        initial_index =0
        for letter in word:
            required_index = keyboard.index(letter)
            total_time += abs(required_index - initial_index)
            initial_index = required_index
        return total_time

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.calculateTime("pqrstuvwxyzabcdefghijklmno","leetcode"))
"""
#################################### Better Code ############################################

class Solution:
    def calculateTime(self, keyboard, word):
        keyboard_dict = {}
        keyboard_value = 0
        for each_letter in keyboard:
            keyboard_dict[each_letter] = keyboard_value
            keyboard_value += 1

        total_time =0
        initial_index =0
        for letter in word:
            required_index = keyboard_dict[letter]
            total_time += abs(required_index - initial_index)
            initial_index = required_index
        return total_time

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.calculateTime("pqrstuvwxyzabcdefghijklmno","leetcode"))