class Node:
    def __init__(self,data = 0):
        self.data = data
        self.left = None
        self.right = None
        self.minDistance= float('inf')

    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<root.data:
                self.insert(root.left,data)
            else:
                self.insert(root.right,data)
            return root
    
    def createTree(self):
        root = None
        print("Enter the Data to form a Tree (-1 to stop)")
        while True:
            data = int(input("ENter the Data : "))
            if data == -1:
                break
            self.insert(root,data)
        return root
    
    def solve(self,root):
        if root is None:
            return float('inf')
        leftans = self.findMinDistance(root.left)
        self.minDistance = min(self.minDistance,root.data-leftans)
        rightAns = self.findMinDistance(root,rightAns)
    
    def findMinDistance(self,root):
        self.solve(root)
        return self.minDistance

l1 = Node()
root = l1.createTree()
ans = l1.findMinDistance(root)
print("Min Distance is : ",ans)