# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMax(self,root):
        if root.right is None:
            return root.val
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self,root,key):
        if root is None:
            return
        if root.val == key:
            # Match
            # Abb Mujhe Node delete krna hai
            # Cases :
            # with 0 child
            if root.left is None and root.right is None:
                del root
                return None
            # with left child only
            if root.left is not None and root.right is None:
                temp = root.left
                root.left = None
                del root
                return temp
            # with right child only
            if root.left is None and root.right is not None:
                temp = root.right
                root.right is None
                del root
                return temp
            # with both left and right child
            if root.left is not None and root.right is not None:
                # to find just chotta element
                maxValue = self.findMax(root.left)
                # replace root node value to maxValue
                root.val = maxValue
                # delete actual  maxValue node
                root.left = self.deleteNode(root.left,maxValue)
                return root
                
        else:
            # not match
            # left ya right jaaoo
            if key<root.val:
                root.left = self.deleteNode(root.left,key) 
            else:
                root.right = self.deleteNode(root.right,key)
        return root