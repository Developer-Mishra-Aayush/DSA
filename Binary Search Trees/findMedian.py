"""
Title: Find Median of BST
Approach: Inorder traversal to collect sorted node values; compute median based on list length (odd/even).
Time: O(n)
Space: O(n)
"""

class Solution:
    def __init__(self):
        self.temp = []
        
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        self.temp.append(root.data)
        self.inorder(root.right)
        
    def findMedian(self, root):
        self.inorder(root)
        n = len(self.temp)
        if n%2!=0:
            return self.temp[n//2]
        
        else:
            # return (self.temp[n//2] + self.temp[n//2 + 1])/2
            mid1 = n // 2 - 1
            mid2 = n // 2
            median =  (self.temp[mid1] + self.temp[mid2])   # use / for float
            if median %2==0:
                return median//2
            else:
                return median/2