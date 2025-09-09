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
        
    def preOrder(self,root):
        if root == None:
            return
        else:
            print(root.data,end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)


l1 = Node()
root = l1.createNode()
l1.preOrder(root)