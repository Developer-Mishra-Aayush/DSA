"""
Title: Level Order Traversal (Left to Right)
Approach: Use BFS with queue, process nodes level by level using None as level separator
Time: O(n) where n is the number of nodes
Space: O(w) where w is maximum width of tree
"""

# Level Order Traversal from left to right
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
    
    def levelOrderTraversal(self,root):
        queue = deque()
        # Inital State Maintain push first Node
        queue.append(root)
        queue.append(None)

        while queue:
            if queue[0]==None:
                queue.popleft()
                print()
                if queue:
                    queue.append(None)
                else:
                    break

            first = queue.popleft()
            print(first.data,end=" ")
            if first.left:
                queue.append(first.left)
            if first.right:
                queue.append(first.right)
l1 = Node()
root = l1.createNode()
l1.levelOrderTraversal(root)
