"""
Title: Postorder Traversal of Binary Tree
Approach: Recursively traverse left subtree, then right subtree, then process root
Time: O(n) where n is the number of nodes
Space: O(h) for recursion stack where h is height
"""

class Node:
    def __init__(self,data= 0):
        self.data = data
        self.left = None
        self.right = None

    def createNode(self):
        data = int(input("Enter the Data : "))
        if data == -1:
            return None
        else:
            root = Node(data)
            print("Add Left Node for data : ",data)
            root.left = self.createNode()
            print("Add Right Node for data : ",data)
            root.right = self.createNode()
            return root
        
    def postOrder(self,root):
        if root == None:
            return
        else:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data,end=" ")


l1 = Node()
root = l1.createNode()
l1.postOrder(root)