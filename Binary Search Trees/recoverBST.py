# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.FV = None
        self.SV = None
        self.prev = None

    def solve(self,root):
        if root is None:
            return

        self.solve(root.left)

        if self.prev is not None and root.val <self.prev.val:
            if self.FV is None:
                self.FV = self.prev
            self.SV = root
        self.prev = root

        self.solve(root.right)

    def recoverTree(self,root):
        self.solve(root)
        if self.FV is not None and self.SV is not None:
            self.FV.val,self.SV.val = self.SV.val,self.FV.val