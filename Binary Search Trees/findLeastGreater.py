"""
Title: Find Least Greater Element on Right (Using BST)
Approach: Traverse array from right to left, insert each element into a BST while tracking its in-order successor during insertion.
Time: O(n log n) average (BST insert + successor), O(n^2) worst-case without balancing
Space: O(n) for BST + O(h) recursion
"""

# Node class for BST
class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def findLeastGreater(self, n, arr):
        result = [-1] * n  # initialize all as -1
        root = None

        # Traverse from right to left
        for i in range(n-1, -1, -1):
            root, successor = self.insert(root, arr[i], None)
            if successor:
                result[i] = successor.val

        return result

    def insert(self, root, val, successor):
        """
        Inserts val into BST rooted at 'root'.
        Returns updated root and in-order successor of val.
        """
        if root is None:
            return BSTNode(val), successor

        if val < root.val:
            # root could be successor
            successor = root
            root.left, successor = self.insert(root.left, val, successor)
        else:
            # go right, successor unchanged
            root.right, successor = self.insert(root.right, val, successor)

        return root, successor
