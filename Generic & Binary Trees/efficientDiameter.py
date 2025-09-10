"""
Title: Diameter of Binary Tree (Efficient)
Approach: Single DFS that returns height while updating a global diameter as max(lh+rh)
Time: O(n)
Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.D = 0
    def height(self,root):
        if root is None:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        currD = lh+rh
        self.D = max(currD,self.D)
        return max(lh,rh)+1

    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.D