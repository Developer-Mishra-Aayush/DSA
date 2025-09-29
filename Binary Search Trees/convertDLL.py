"""
Title: Convert BST to Sorted Doubly Linked List
Approach: Reverse inorder traversal (RNL); relink nodes in-place using a moving head pointer to form a DLL.
Time: O(n)
Space: O(h)
"""

class Node:

    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.head = None
        
    def solve(self,root):
        if root is None:
            return 
        
        # RNL
        self.solve(root.right)
        # assume kr skte hu , k right part ki ll bangaee hai 
        # and head k right part ki ll k start node pr hoga
        
        root.right = self.head
        if self.head is not None:
            self.head.left = root
            
        # head ko update krna hai
        self.head = root
        # abb tree ka left part pending hai
        self.solve(root.left)
    
    def bToDLL(self,root):
        self.solve(root)
        return self.head