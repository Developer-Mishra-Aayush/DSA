"""
Title: Convert Binary Tree to Sum Tree
Approach: Postorder DFS; for each node, compute sum of left and right subtrees, set node.data to that sum, and return old node value + new node.data to parent
Time: O(n)
Space: O(h)
"""

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def solve(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            temp = root.data
            root.data = 0
            return temp
        lsum = self.solve(root.left)
        rsum = self.solve(root.right)
        
        temp = root.data
        root.data = lsum + rsum
        return root.data + temp
        
    def toSumTree(self, root) :
        self.solve(root)