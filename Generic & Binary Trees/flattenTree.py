"""
Title: Flatten Binary Tree to Linked List
Approach: Morris-like traversal; for each node with left child, find rightmost node in left subtree and connect it to current's right, then move left to right.
Time: O(n)
Space: O(1)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def flatten(self,root):
        curr = root
        while curr:
            if curr.left:
                pred = curr
                pred = curr.left
                while pred.right:
                    pred = pred.right
                pred.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right