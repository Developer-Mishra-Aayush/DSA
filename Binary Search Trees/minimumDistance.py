class Node:
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None
        self.minDistance= float('inf')
        self.pre = None

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
    
    def solve(self,root):
        # Do this Question By Using inorder Traversal
        if root is None:
            return

        # Left Call
        self.solve(root.left)
        if self.prev is not None:
            self.minDistance = min(self.minDistance,abs(root.val - self.prev.val))
        # Now Place the Prev to Curr
        self.prev = root

        # Right Call
        self.solve(root.right)
    
    def findMinDistance(self,root):
        self.solve(root)
        return self.minDistance

l1 = Node()
root = l1.createTree()
ans = l1.findMinDistance(root)
print("Min Distance is : ",ans)