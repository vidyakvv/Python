"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive,
so "a" is considered a different type of stone from "A".

Input: J = "aA", S = "aAAbbbb"
Output: 3
"""



class Solution:
    def numJewelsinStones(self, J: str, S: str) -> int :
        count = 0
        for stone in S:
            if stone in J:
                count += 1

        return count



if __name__ == "__main__":
    my_solution = Solution();
    print(my_solution.numJewelsinStones("aA", "aAAbbbb"))