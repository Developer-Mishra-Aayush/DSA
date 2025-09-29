"""
Title: Balance a Binary Search Tree
Approach: Inorder traverse BST to collect sorted values, then build a balanced BST by recursive mid selection (sorted array to BST).
Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.temp = []
    
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.temp.append(root.val)
        self.inorder(root.right)

    def createTree(self,start,end):
        if start>end:
            return

        mid = start + (end - start)//2
        root = TreeNode(self.temp[mid])
        root.left = self.createTree(start,mid - 1)
        root.right = self.createTree(mid+1,end)

        return root

    def balanceBST(self,root):
        self.inorder(root)
        return self.createTree(0,len(self.temp)-1)