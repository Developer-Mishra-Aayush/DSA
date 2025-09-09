from collections import deque

class Node:
    def __init__(self, data=0):
        self.data = data
        self.left = None
        self.right = None

    def createNode(self):
        data = int(input("Enter the Data : "))
        if data == -1:
            return None
        else:
            root = Node(data)
            print("Enter Left Node of data:", data)
            root.left = self.createNode()
            print("Enter Right Node of data:", data)
            root.right = self.createNode()
            return root
    
    def levelOrderTraversalRightToLeft(self, root):
        if not root:
            return

        queue = deque()
        queue.append(root)
        queue.append(None)  # level marker

        while queue:
            node = queue.popleft()

            if node is None:
                print()  # end of one level
                if queue:
                    queue.append(None)  # marker for next level
            else:
                print(node.data, end=" ")
                # ✅ enqueue right first, then left
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)


# Example usage
l1 = Node()
root = l1.createNode()
print("\nLevel Order Traversal (Right → Left, line by line):")
l1.levelOrderTraversalRightToLeft(root)
