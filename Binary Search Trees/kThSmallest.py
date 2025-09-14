from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = deque()
    
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self,root,k):
        self.inorder(root)
        return self.ans[k-1] 