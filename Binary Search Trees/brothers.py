"""
Title: Brothers From Different Trees (Pairs Summing to Target)
Approach: Inorder traverse Tree1 and Tree2 (reverse) to get sorted lists; two-pointer to find pairs summing to target.
Time: O(n + m)
Space: O(n + m)
"""

class Node:
    def __init__(self,data = 0):
        self.data = data
        self.left = None
        self.right = None
        self.first = []
        self.second = []
        self.ans = []

    def insert(self,root,val):
        if root is None:
            return Node(val)
        else:
            if val<root.data:
                root.left = self.insert(root.left,val)
            else:
                root.right = self.insert(root.right,val)
            return root

    def createTree(self):
        print("Enter the Data to create a Tree (-1 to stop) : ")
        root = None
        while True:
            val = int(input("Enter the Data : "))
            if val == -1:
                break
            else:
                root = self.insert(root,val)
        return root
    
    def inorderFirst(self,root):
        if root is None:
            return
        
        self.inorderFirst(root.left)
        self.first.append(root.data)
        self.inorderFirst(root.right)

    def inorderSecond(self,root):
        if root is None:
            return
        
        self.inorderSecond(root.left)
        self.second.append(root.data)
        self.inorderSecond(root.right)

    def findBrothers(self,root1,root2,target):
        # Step 1 : Create a Inorder traversal of both Tree
        self.inorderFirst(root1)
        self.inorderSecond(root2)
        self.second = self.second[::-1]
        i = 0
        j = 0
        while i<len(self.first) and j<len(self.second):
            if i<len(self.first) and j<len(self.second) and self.first[i]+self.second[j]==target:
                self.ans.append((self.first[i],self.second[j]))
                i+=1
            if i<len(self.first) and j<len(self.second) and self.first[i]+self.second[j]>target:
                j+=1
            else:
                i+=1

    
l1 = Node()
l2 = Node()
print("Creating First Tree : ")
root1 = l1.createTree()
print("Creating Second tree : ")
root2 = l2.createTree()
l1.findBrothers(root1,root2,16)
print("Total Possible Brothers are : ",l1.ans)