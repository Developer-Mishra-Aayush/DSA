# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getLength(self,head):
        temp = head
        i = 0
        while temp:
            i+=1
            temp = temp.next
        return i

    def solve(self,n):
        if self.head is None or n<=0:
            return None

        # LNR
        leftTree = self.solve(n//2)
        # N - Process the Current Node
        root = TreeNode(self.head.val)
        root.left = leftTree

        # Abb Head koh aage badhaoo
        self.head = self.head.next

        # R - Right Tree koh process karo
        rightTree = self.solve(n-n/2-1)
        root.right = rightTree

        return root

    def sortedListToBST(self, head):
        n = self.getLength(head)
        self.head = head
        root = self.solve(n)
        return root