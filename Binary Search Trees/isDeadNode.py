"""
Title: Check Dead End in BST
Approach: Inorder to collect all node values into a set; a leaf is dead-end if both (val-1) and (val+1) exist (with 1 as a special case).
Time: O(n)
Space: O(n)
"""

class Solution:
    def __init__(self):
        self.temp = set()
    
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.temp.add(root.data)
        self.inorder(root.right)
        
    def checkDeadEnd(self,root):
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            # Check dead-end condition
            # 1 is a special case: cannot insert 0
            if (root.data == 1 and (root.data + 1) in self.temp) or \
               (root.data != 1 and (root.data - 1) in self.temp and (root.data + 1) in self.temp):
                return True
                
        leftAns = self.checkDeadEnd(root.left)
        rightAns = self.checkDeadEnd(root.right)
        return leftAns or rightAns
        
    def isDeadEnd(self, root):
        self.inorder(root)
        return self.checkDeadEnd(root)