""" Given the root node of a binary search tree,
return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node):
            if node:
                if L <= node.val <=  R:
                    self.sum += node.val
                if node.val < R:
                    dfs(node.right)
                if node.val > L:
                    dfs(node.left)
        self.sum = 0
        dfs(root)
        return self.sum

if __name__ == "__main__":

    my_solution = Solution()
    print(my_solution.rangeSumBST(root = [10,5,15,3,7,None,18], L = 7, R = 15))
    #print(sum([1,1,2,3]))











