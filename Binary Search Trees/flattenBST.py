"""
Title: Flatten BST to Sorted Right-Skewed List
Approach: Inorder traversal; maintain a dummy and previous pointer, relink nodes' right pointers in sorted order and set left to None.
Time: O(n)
Space: O(h)
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.dummy= Node(-1)
        self.prev = self.dummy
        
    def flattenBST(self, root):
        if root is None:
            return
        
        self.flattenBST(root.left)
        
        self.prev.left = None
        self.prev.right = root
        self.prev = root
        root.left = None
        
        self.flattenBST(root.right)
        self.prev.right = None
        return self.dummy.right