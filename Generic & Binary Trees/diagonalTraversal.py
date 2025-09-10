"""
Title: Diagonal Traversal of Binary Tree
Approach: Use a map of diagonal index -> nodes; recurse with (left -> index+1, right -> index) and collect lists
Time: O(n)
Space: O(n)
"""

from collections import deque

class Node:
    def __init__(self,data = 0):
        self.data = data
        self.left = None
        self.right = None

    def createNode(self):
        data = int(input("Enter the Data : "))
        if data == -1:
            return None
        else:
            root = Node(data)
            print("Enter Left Node of data : ",data)
            root.left = self.createNode()
            print("Enter Right Node of data : ",data)
            root.right = self.createNode()
            return root
        
    def printDiagonal(self,dict,root,index):
        if root is None:
            return 
        if index not in dict:
            dict[index] = []
        dict[index].append(root.data)
        self.printDiagonal(dict,root.left,index+1)
        self.printDiagonal(dict,root.right,index)

        
    def diagonalTraversal(self,root):
        dict = {}
        index = 0
        self.printDiagonal(dict,root,index)
        return dict.values()

    
l1 = Node()
root = l1.createNode()
ans = l1.diagonalTraversal(root)
print(ans)