"""
Title: Construct Binary Tree from Inorder and Postorder Traversal
Approach: Use a hashmap for inorder indices and a postorder index pointer (starting from end); recursively build right then left subtree
Time: O(n)
Space: O(n)
"""

# Constructing Tree From Inorder and Postorder
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.postorderIndex = 0

    def createMapping(self,inorder):
        dict = {}
        for i,val in enumerate(inorder):
            dict[val] = i
        return dict

    def createTree(self,dict,inorder,postorder,inorderStartIndex,inorderEndIndex):
        if inorderStartIndex>inorderEndIndex:
            return None
        if self.postorderIndex<0:
            return None

        # Now Compute for the Left Item of postorder as a root
        root = TreeNode(postorder[self.postorderIndex])

        inorderPositionIndex = dict[postorder[self.postorderIndex]]
        self.postorderIndex-=1

        root.right = self.createTree(dict,inorder,postorder,inorderPositionIndex+1,inorderEndIndex)
        root.left = self.createTree(dict,inorder,postorder,inorderStartIndex,inorderPositionIndex-1)

        return root
        

    def buildTree(self, inorder, postorder):
        dict = {}
        dict = self.createMapping(inorder)
        self.postorderIndex = len(postorder)-1
        return self.createTree(dict,inorder,postorder,0,len(postorder)-1)