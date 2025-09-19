class Node:
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None
        self.pred = None

    def insert(self,root,val):
        if root is None:
            return Node(val)
        else:
            if val<root.val:
                root.left = self.insert(root.left,val)
            else:
                root.right = self.insert(root.right,val)
            return root
    
    def createTree(self):
        root = None
        print("Enter the Data to form a Tree (-1 to stop)")
        while True:
            val = int(input("ENter the Data : "))
            if val == -1:
                break
            root = self.insert(root,val)
        return root
    
    def solve(self,root,target):
        if root is None:
            return
        
        if root.data ==target:
            return 
        
        if root.data<target:
            self.pred = root.data
            self.solve(root.right,target)
        if root.data>target:
            self.solve(root.left,target)
        return self.pred
    
    def findPredecessor(self,root,target):
        self.solve(root,target)
        return self.pred


l1 = Node()
root = l1.createTree()