"""
Title: Find Duplicate Subtrees
Approach: Serialize each subtree using preorder traversal; use a map to track frequency and collect duplicates.
Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.dict = {}
        self.ans = []
        
    def preorder(self,root):
        if root is None:
            return 'N'
        
        N = str(root.val)
        L = self.preorder(root.left)
        R = self.preorder(root.right)
        NLR = N + ',' + L + ',' + R
        if NLR in self.dict:
            if self.dict[NLR]==1:
                self.ans.append(root)
            self.dict[NLR]+=1
        else:
            self.dict[NLR] = 1

        return NLR         

    def findDuplicateSubtrees(self,root):
        self.preorder(root)
        return self.ans