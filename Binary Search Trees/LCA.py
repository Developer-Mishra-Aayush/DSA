# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self,root,p,q):
        if root is None:
            return None
        if root.val is p.val:
            return p
        if root.val is q.val:
            return q
        
        leftAns = self.lowestCommonAncestor(root.left,p,q)
        rightAns = self.lowestCommonAncestor(root.right,p,q)

        if leftAns is None and rightAns is None:
            return None
        if leftAns is None and rightAns is not None:
            return rightAns
        if rightAns is None and leftAns is not None:
            return leftAns
        else:
            return root