"""
Title: Construct Binary Tree from Preorder and Inorder Traversal
Approach: Use a hashmap for inorder indices and a preorder index pointer; recursively build left and right subtrees based on inorder partition
Time: O(n)
Space: O(n)
"""

# Construct Tree from Inorder and Preorder
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.preorderIndex = 0
    def createMapping(self,inorder,dict):
        for i,val in enumerate(inorder):
            dict[val] = i

    def createTree(self,dict,preorder,inorder,inorderStart,inorderEnd,size):
        if self.preorderIndex>=size:
            return None
        if inorderStart>inorderEnd:
            return None
        
        # process the first element of preorder as a root
        root = TreeNode(preorder[self.preorderIndex])
        elementIndex = dict[preorder[self.preorderIndex]]
        self.preorderIndex+=1

        root.left = self.createTree(dict,preorder,inorder,inorderStart,elementIndex-1,size)
        root.right = self.createTree(dict,preorder,inorder,elementIndex+1,inorderEnd,size)

        return root

    def buildTree(self, preorder, inorder):
        dict = {}
        self.createMapping(inorder,dict)
        root = self.createTree(dict,preorder,inorder,0,len(preorder)-1,len(preorder))
        return root