"""
Title: Path Sum II (All Root-to-Leaf Paths Equal to Target)
Approach: DFS with backtracking; accumulate path and current sum, append copy when leaf matches target, backtrack after exploring children
Time: O(n) nodes visited; path copy cost across all matches may add up but bounded by O(n * number_of_paths)
Space: O(h) recursion + O(k) for path storage
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def solve(self,root,targetSum,currentSum,tempAns,ans):
        if root is None:
            return None

        tempAns.append(root.val)
        if root.left is None and root.right is None and currentSum+root.val== targetSum:
            ans.append(tempAns[:])
        
        self.solve(root.left,targetSum,currentSum+root.val,tempAns,ans)
        self.solve(root.right,targetSum,currentSum+root.val,tempAns,ans)

        tempAns.pop()

    def pathSum(self, root, targetSum):
        ans = []
        tempAns = []
        currentSum = 0
        self.solve(root,targetSum,currentSum,tempAns,ans)
        return ans