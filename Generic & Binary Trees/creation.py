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
            print("Adding left child for data : ",data)
            root.left = self.createNode()
            print("Adding right child for data : ",data)
            root.right = self.createNode()
            return root
        
l1 = Node()
l1.createNode()