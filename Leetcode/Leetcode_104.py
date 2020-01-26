"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

return its depth = 3.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs1(node):
    if not node :
        return 0
    else:
        return max(dfs1(node.right), dfs1(node.left) ) +1


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return dfs1(root)

""" *** Iterative Solution****
class Solution:
    def maxDepth(self, root):
        
        #:type root: TreeNode
        #:rtype: int
        
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth
"""