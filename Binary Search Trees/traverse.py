from collections import deque
class Node:
    def __init__(self,data= 0):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,root,data):
        if root is None:
            return Node(data)
        else:
            if data<root.data:
                root.left = self.insert(root.left,data)
            else:
                root.right = self.insert(root.right,data)
            return root

    def createTree(self):
        print("Enter numbers to insert into BST (-1 to stop):")
        root = None
        while True:
            data = int(input("Enter the Data : "))
            if data == -1:
                break
            root = self.insert(root,data)

        return root
    
    def levelOrderTraverse(self,root):
        if root is None:
            return
        else:
            queue = deque()
            queue.append(root)
            while queue:
                temp = queue.popleft()
                print(temp.data,end=" ")
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)

    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
    
    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")
    
l1 = Node()
root = l1.createTree()
l1.levelOrderTraverse(root)
print('\n')
print("########### Inorder traversal ###########")
l1.inorder(root)
print("########### Preorder traversal ###########")
l1.preorder(root)
print("########### Postorder traversal ###########")
l1.postorder(root)