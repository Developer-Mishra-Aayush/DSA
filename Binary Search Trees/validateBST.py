# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self,root):
        # Apply PostOrder To Solve this Question
        if root is None:
            return True,float('-inf'),float('inf')

        # Traverse Left Part
        isLeftBst,leftMax,leftMin = self.solve(root.left)

        # Traverse Right Part
        isRightBst,rightMax,rightMin = self.solve(root.right)

        # Check Whether the Current Subtree Is Valid or not
        if isLeftBst and isRightBst and root.val >leftMax and root.val<rightMin:
            return True,max(root.val,rightMax),min(root.val,leftMin)
        else:
            return False,float('inf'),float('-inf')

    def isValidBST(self,root):
        ans,_,_ = self.solve(root)
        return ans
        