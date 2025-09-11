# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self,root):
        ans = []
        curr = root
        while curr:
            # If left node is None them mark the item and go to right
            if curr.left is None:
                ans.append(curr.val)
                curr = curr.right
            # Left node is not None
            else:
                pred = curr.left
                while pred.right!=curr and pred.right is not None:
                    pred = pred.right
                # if pred right is none then go left after establishing link from pred to curr
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    ans.append(curr.val)
                    pred.right = None
                    curr = curr.right
        return ans