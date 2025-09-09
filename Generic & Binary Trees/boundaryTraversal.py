"""
Title: Boundary Traversal of Binary Tree
Approach: Collect root, left boundary (excluding leaves), all leaves (left then right), and right boundary in reverse
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
    
    def traverseBoundary(self,root):
        ans = []
        if root is None:
            return ans
        
        # First Append Root Node
        ans.append(root.data)

        # First Root Left Boundary
        self.rootLeftBoundary(root.left,ans)

        # Second Root Left Leaf Boundary
        self.leafBoundary(root.left,ans)

        # Third Root Right Leaf Boundary
        self.leafBoundary(root.right,ans)

        # Fourth Root RIght Boundary In Reverse
        self.rootRightBoundary(root.right,ans)
        return ans

l1 = Node()
root = l1.createNode()
ans = l1.traverseBoundary(root)
print(ans)