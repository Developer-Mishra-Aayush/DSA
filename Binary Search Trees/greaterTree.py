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

    def allRightSum(self):
        for i in range(len(self.ans)-2,-1,-1):
            self.ans[i] = self.ans[i] + self.ans[i+1]
        

    def reassignTree(self,root):
        if root is None:
            return
        self.reassignTree(root.left)
        root.val = self.ans[0]
        self.ans.popleft()
        self.reassignTree(root.right)
    
        
    def bstToGst(self,root):
        self.inorder(root)
        self.allRightSum()
        self.reassignTree(root)
        return root