"""
Title: Maximum Depth of Binary Tree
Approach: Recursively compute height as 1 + max(height(left), height(right)); base: None -> 0
Time: O(n) where n is number of nodes
Space: O(h) recursion stack (h = height)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        leftheight = self.maxDepth(root.left)
        rightheight = self.maxDepth(root.right)
        maxHeight= max(leftheight,rightheight)
        ans = maxHeight + 1
        return ans