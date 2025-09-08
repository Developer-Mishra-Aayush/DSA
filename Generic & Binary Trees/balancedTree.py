# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root == None:
            return 0
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        maxHeight = max(leftHeight,rightHeight)
        return maxHeight + 1

    def isBalanced(self, root):
        if root == None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        absDiff = abs(rh-lh)
        status = True if absDiff<=1 else False

        leftAns = self.isBalanced(root.left)
        rightAns = self.isBalanced(root.right)

        if status and leftAns and rightAns:
            return True
        else:
            return False