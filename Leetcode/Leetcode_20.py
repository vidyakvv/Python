


class Solution:
    def isValid(self, s: str) -> bool:
        """
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
        """
        """ ******** Using Stack - Faster Solution """
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        stack = []
        for i in s:
            if i in open_par:
                stack.append(i)
            elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []


if __name__ == "__main__":
    my_solution = Solution()
    print(my_solution.isValid("{{()()[[{{{()()}()}[]}]()]}}"))