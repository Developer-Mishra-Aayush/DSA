"""
Title: Sum of Longest Bloodline (Root to Leaf Path)
Approach: DFS to find all root-to-leaf paths; track the longest path and among those, the one with maximum sum.
Time: O(n)
Space: O(h)
"""

'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def __init__(self):
        self.sumi = 0
        self.ans = []
    
    def solve(self,root,tempAns):
        if root is None:
            return 
        if root.left is None and root.right is None:
            tempAns.append(root.data)
            if len(tempAns)==len(self.ans) and sum(tempAns)>self.sumi:
                self.ans = tempAns[:]
                self.sumi = sum(self.ans)
            elif len(tempAns)>len(self.ans):
                self.ans = tempAns[:]
                self.sumi = sum(self.ans)
            return
        
        else:
            self.solve(root.left,tempAns+[root.data])
            self.solve(root.right,tempAns+[root.data])
                

    def sumOfLongRootToLeafPath(self, root):
        tempAns = []
        self.solve(root,tempAns)
        return self.sumi