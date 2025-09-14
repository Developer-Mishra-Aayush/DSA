# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def solve(self,nums,s,e):
        if s>e:
            return None
        mid = (s+e)//2
        element = nums[mid]
        root = TreeNode(element)
        root.left = self.solve(nums,s,mid-1)
        root.right = self.solve(nums,mid+1,e)
        return root
        
    def sortedArrayToBST(self, nums):
        s = 0
        e = len(nums)-1
        root = self.solve(nums,s,e)
        return root