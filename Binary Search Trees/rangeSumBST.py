"""
Title: Range Sum of BST
Approach: Inorder traversal; add node values that fall within [low, high]. Can be optimized by pruning branches.
Time: O(n) (O(k) with pruning where k is visited nodes)
Space: O(h)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self,root,low,high):
        if root is None:
            return
        self.rangeSumBST(root.left,low,high)
        if root.val >=low and root.val<=high:
            self.sum+=root.val
        self.rangeSumBST(root.right,low,high)

        return self.sum