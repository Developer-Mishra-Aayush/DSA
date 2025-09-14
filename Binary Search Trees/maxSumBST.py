# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.maxSum = 0
    def getMax(self,root):
        if not root:
            # Return Max Value,Min Value and Total Sum , Valid BST
            return (float('-inf'),float('inf'),0)
        # Traverse Left And Right Part
        leftMax,leftMin,leftMaxSum = self.getMax(root.left)
        rightMax,rightMin,rightMaxSum = self.getMax(root.right)

        # If A valid BST
        if root.val>leftMax and root.val<rightMin:
            # Update MaxSum
            self.maxSum = max(self.maxSum,root.val + leftMaxSum + rightMaxSum)
            return max(root.val,rightMax),min(root.val,leftMin),root.val + leftMaxSum + rightMaxSum
        # If Not a valid BST
        else:
            return (float('inf'),float('-inf'),0)

    def maxSumBST(self, root):
        self.getMax(root)
        return self.maxSum