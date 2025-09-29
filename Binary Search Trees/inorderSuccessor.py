"""
Title: Inorder Successor in BST
Approach: Traverse from root; when node.data > target, record as candidate and go left, else go right.
Time: O(h)
Space: O(1)
"""

class Node:
    def __init__(self,data = 0):
        self.data = data
        self.left = None
        self.right = None
        self.success = None

    def insert(self,root,val):
        if root is None:
            return Node(val)
        else:
            if val < root.data:
                root.left = self.insert(root.left,val)
            else:
                root.right = self.insert(root.right,val)
            return root

    def createTree(self):
        print("Enter the data to create a tree (-1 to stop) : ")
        root = None
        while True:
            val = int(input("Enter the Data : "))
            if val == -1:
                break
            else:
                root = self.insert(root,val)
        return root
    
    def inorderSuccessor(self,root,targetNode):
        # Base Case
        if root is None:
            return
        else:
            if root.data >targetNode:
                self.success = root
                print("Getting answer")
                self.inorderSuccessor(root.left,targetNode)
            else:
                self.inorderSuccessor(root.right,targetNode)
    
l1 = Node()
root = l1.createTree()
targetNode = 7
l1.inorderSuccessor(root,targetNode)
print(f"The inorderPredecessor of Node {targetNode} is {l1.success.data}")