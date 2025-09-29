"""
Title: Top View of Binary Tree
Approach: Traverse left subtree in reverse order, then right subtree in normal order; collect nodes visible from top.
Time: O(n)
Space: O(h)
"""

# Traverse Top View of the Tree

class Node:
    def __init__(self,data =0):
        self.data = data
        self.left = None
        self.right = None
    
    def createNode(self):
        data = int(input("Enter the Data : "))
        if data ==-1:
            return None
        root = Node(data)
        print("Adding Left Node for ",data," : ")
        root.left = self.createNode()
        print("Adding Right Node for ",data," : ")
        root.right = self.createNode()
        return root
    
    def leftTree(self,root,ans):
        if root is None:
            return
        
        self.leftTree(root.left,ans)
        ans.append(root.data)

    def rightTree(self,root,ans):
        if root is None:
            return
        
        ans.append(root.data)
        self.rightTree(root.right,ans)
    
    def topView(self,root):
        ans = []
        if root is None:
            return ans

        # First Traverse to the left Tree
        self.leftTree(root,ans)

        # Second Traverse to the Right Tree
        self.rightTree(root.right,ans)

        return ans

    
    

l1 = Node()
root = l1.createNode()
ans = l1.topView(root)
print(ans)