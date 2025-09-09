"""
Title: Left View of Binary Tree
Approach: DFS preorder tracking first node seen at each level; when level equals answer size, append node
Time: O(n)
Space: O(h)
"""

class Node:
    def __init__(self,data =0):
        self.data = data
        self.left = None
        self.right = None
    
    def createNode(self):
        data = int(input("Enter the Data : "))
        if data ==-1:
            return None
        root = Node(data)
        print("Adding Left Node for ",data," : ")
        root.left = self.createNode()
        print("Adding Right Node for ",data," : ")
        root.right = self.createNode()
        return root
    
    def rootLeftBoundary(self,root,ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        ans.append(root.data)
        self.rootLeftBoundary(root.left,ans)

    def leafBoundary(self,root,ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            ans.append(root.data)
        self.leafBoundary(root.left,ans)
        self.leafBoundary(root.right,ans)
    
    def rootRightBoundary(self,root,ans):
        if root is None:
            return
        if root.left is None and root.right is None:
            return
        self.rootRightBoundary(root.right,ans)
        ans.append(root.data)

    def solveleftView(self,root,ans,level):
        if root is None:
            return
        if level == len(ans):
            ans.append(root.data)
        self.solveleftView(root.left,ans,level+1)
        self.solveleftView(root.right,ans,level+1)
        

    def leftView(self,root):
        ans = []
        level = 0
        self.solveleftView(root,ans,level)
        return ans
    
   

l1 = Node()
root = l1.createNode()
ans = l1.leftView(root)
print(ans)