"""
Title: Path Sum III (Count Paths with Sum K)
Approach: For each node, count paths starting at that node via DFS; recurse on children to consider all starting points
Time: O(n^2) worst-case; can be O(n) with prefix-sum optimization
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
        self.count = 0

    def solve(self,root,targetSum):
        if root is None:
            return
        if root.val == targetSum:
            self.count+=1
        self.solve(root.left,targetSum-root.val)
        self.solve(root.right,targetSum-root.val)

    def pathSum(self,root,targetSum):
        if root:
            self.solve(root,targetSum)
            self.pathSum(root.left,targetSum)
            self.pathSum(root.right,targetSum)
        return self.count