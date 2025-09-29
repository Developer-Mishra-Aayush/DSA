"""
Title: Construct BST from Preorder Traversal
Approach: Insert preorder values into BST one by one; alternative is bounded recursion using value ranges.
Time: O(n^2) worst-case (skewed), O(n log n) average; O(n) with bounds method
Space: O(h)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def createTree(self,root,data):
        # Base Case
        if root is None:
            return TreeNode(val = data)
        else:
            if data <root.val:
                root.left = self.createTree(root.left,data)
            else:
                root.right = self.createTree(root.right,data)
            return root
    def bstFromPreorder(self, preorder):
        root = None
        for i in preorder:
            root = self.createTree(root,i)
        return root