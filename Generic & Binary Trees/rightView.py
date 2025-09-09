"""
Title: Right View of Binary Tree
Approach: DFS preorder prioritizing right child; record first node visited at each level
Time: O(n)
Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solvelrightView(self,root,ans,level):
        if root is None:
            return
        if level == len(ans):
            ans.append(root.val)
        self.solvelrightView(root.right,ans,level+1)
        self.solvelrightView(root.left,ans,level+1)

    def rightSideView(self, root):
        ans = []
        level = 0
        self.solvelrightView(root,ans,level)
        return ans