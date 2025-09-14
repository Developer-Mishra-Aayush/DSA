# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = []

    def inorderTraversal(self,root):
        if root is None:
            return
        else:
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
        
    def findTarget(self,root,k):
        self.inorderTraversal(root)
        start = 0
        end = len(self.ans)-1
        while start<end:
            if start<end and self.ans[start] + self.ans[end] == k:
                return True
            elif start<end and self.ans[start] + self.ans[end]<k:
                start+=1
            elif start<end and self.ans[start] + self.ans[end]>k:
                end-=1
            else:
                return False
        return False