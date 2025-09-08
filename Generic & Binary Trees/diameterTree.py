from functools import lru_cache
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @lru_cache(None)
    def getHeight(self,root):
        if root == None:
            return 0
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        maxHeight = max(leftHeight,rightHeight)
        return maxHeight + 1
        
    def diameterOfBinaryTree(self, root):
        if root == None:
            return 0
        option1 = self.diameterOfBinaryTree(root.left)
        option2 = self.diameterOfBinaryTree(root.right)
        option3 = self.getHeight(root.left) + self.getHeight(root.right)
        return max(option1,max(option2,option3))