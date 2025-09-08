"""
Title: Path Sum (Root to Leaf)
Approach: DFS recursively subtracting node values from target; check at leaves if remaining sum is zero
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
    def hasPathSum(self, root, targetSum):
        if root is None :
            return False
        
        if targetSum - root.val == 0 and root.left is None and root.right is None:
            return True

        leftAns = self.hasPathSum(root.left,targetSum-root.val)
        rightAns = self.hasPathSum(root.right,targetSum-root.val)

        return leftAns or rightAns