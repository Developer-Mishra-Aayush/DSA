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