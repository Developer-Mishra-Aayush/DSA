class Node:
    def __init__(self,data = 0):
        self.left = None
        self.right = None
        self.data = data
        self.pred = None

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
        print("Enter the Data to form a Tree(-1 to stop)")
        root = None
        while True:
            val = int(input("Enter the Data : "))
            if val == -1:
                break
            root  = self.insert(root,val)
        return root
    
    def inorderPredecessor(self,root,targetnode):
        # Base Case
        if root is None:
            return
        else:
            if root.data<targetNode:
                self.pred = root
                self.inorderPredecessor(root.right,targetNode)
            else:
                self.inorderPredecessor(root.left,targetNode)
        

l1 = Node()
root = l1.createTree()
targetNode = 8
l1.inorderPredecessor(root,targetNode)
print(f"Inorder Predeceddor of Node {targetNode} is {l1.pred.data}")