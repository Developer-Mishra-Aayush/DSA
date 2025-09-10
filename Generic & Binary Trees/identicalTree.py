"""
Title: Identical Binary Trees
Approach: Recursively compare structure and node values for both trees; ensure both subtrees match
Time: O(n)
Space: O(h)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # Base case
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val!=q.val:
            return False
        if (p.left is None and q.left is not None)  or (p.left is not None and q.left is None) or (p.right is None and q.right is not None) or (p.right is not None and q.right is None):
            return False

        # First  Case go for left Subtree
        first = self.isSameTree(p.left,q.left)

        # Second Case go for right Subtree
        second = self.isSameTree(p.right,q.right)

        return first and second