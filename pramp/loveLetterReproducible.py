"""class Solution:
    def isLoveLetterReproducible(self, L, M) -> bool :
        L_map ={}
        L_ind_letter = 0
        for letter in L:
            if letter in L_map:
                L_map[letter] += 1
            else:
                L_map[letter] = 1
                L_ind_letter += 1
        print(L_map)
        print(L_ind_letter)
        M_map ={}
        for letter in M:
            if letter in M_map:
                M_map[letter] += 1
            else:
                M_map[letter] = 1
        print(M_map)

        loop_count=0
        for letter in L:
            if M_map[letter] >= L_map[letter]:
                loop_count += 1
                if(L_ind_letter == loop_count):
                    return True
            else:
                return False


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.isLoveLetterReproducible("Love you Love you Love you", "Love you Love you Loveyoumore"))
"""
###################################################################################################
class Solution:
    def isLoveLetterReproducible(self, L, M) -> bool :
        L_map ={}
        count_letters = len(L)
        for letter in L:
            if letter in L_map:
                L_map[letter] += 1
            else:
                L_map[letter] = 1
        print(L_map)

        M_map ={}
        for letter in M:

            if letter not in L_map:
                continue
            else:
                count_letters -= 1
                L_map[letter] -= 1
                print(L_map)

        for letter in L_map:
            if L_map[letter] > 0:
                return False

        return True

if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.isLoveLetterReproducible("Love you Love you Love you", "more and more Love you Love you Love youmore"))