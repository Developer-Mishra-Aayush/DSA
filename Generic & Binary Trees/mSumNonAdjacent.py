"""
Title: Maximum Sum of Non-Adjacent Nodes in Binary Tree
Approach: For each node, return [sum_including_node, sum_excluding_node]; take max of both options at root.
Time: O(n)
Space: O(h)
"""

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    def solve(self,root):
        if root is None:
            return [0,0]
            
        left = self.solve(root.left)
        right = self.solve(root.right)
        
        # Sum Including the Node
        a = root.data + left[1] + right[1]
        
        # Sum Excluding the Node
        b = max(left) + max(right)
        return [a,b]
        
    def getMaxSum(self, root):
        ans = self.solve(root)
        return max(ans)