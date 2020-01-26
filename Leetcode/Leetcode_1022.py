"""
Given a binary tree, each node has value 0 or 1.
Each root-to-leaf path represents a binary number starting with the most significant bit.
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Input: [1,0,1,0,1,0,1] -> preorder traversal
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def dfs2(node, parent_sum=None):
        if parent_sum == None:
            parent_sum = 0
        if node:
            parent_sum = parent_sum * 2 + node.val
            if node.left or node.right:
                return dfs2(node.left, parent_sum) + dfs2(node.right, parent_sum)
            else:
                return parent_sum
        else:
                return 0

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return dfs2(root)