from collections import deque
class Node:
    def __init__(self,data = 0):
        self.data = data
        self.left = None
        self.right = None
        self.time = 0
        self.mapParent = {}
        self.totalLength  = 0

    def createTree(self):
        data = int(input("Enter the Data : "))
        if data == -1:
            return None
        root = Node(data)
        print("Enter Left Node of Data ",data," : ")
        root.left = self.createTree()
        print("Ente Right Node of Data ",data," : ")
        root.right = self.createTree()
        return root
    
    def findAndMake(self,root,target):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        self.mapParent[root.data] = None
        while queue:
            temp = queue.popleft()
            if temp.data == target:
                targetNode = temp
            if temp.left:
                queue.append(temp.left)
                self.mapParent[temp.left.data] = temp.data
            if temp.right:
                queue.append(temp.right)
                self.mapParent[temp.right.data] = temp.data
        self.totalLength = len(self.mapParent)
        return targetNode
    
    def nowStartBurning(self, root, target):
        alreadyBurn = [target.data]
        while len(alreadyBurn) != self.totalLength:
            tempAns = []

            # First Try To Burn the Parent Node
            for i in list(self.mapParent):
                if i in alreadyBurn:
                    if self.mapParent[i] is not None:
                        tempAns.append(self.mapParent[i])
                    del self.mapParent[i]

            # Second Try To Burn the Child Node
            for i in list(self.mapParent):
                if self.mapParent[i] in alreadyBurn:
                    tempAns.append(i)
                    del self.mapParent[i]

            self.time += 1
            alreadyBurn.extend(tempAns)
    
    def getTimetoBurn(self,root,target):
        if root is None:
            return 0
        
        # Step 1 : Find the Target Node and Make a Node to Parent Node Dictionary
        targetNode = self.findAndMake(root,target)

        # Step 2 : Now Burn the Tree
        self.nowStartBurning(root,targetNode)
        return self.time
    
l1 = Node()
root = l1.createTree()
ans = l1.getTimetoBurn(root,2)
print("Total Time to Burn a Tree is : ",ans)