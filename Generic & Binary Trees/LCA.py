"""
Title: Lowest Common Ancestor of a Binary Tree
Approach: Recurse from root; if a node matches p or q, return it; otherwise return non-null result from left/right; if both non-null, current is LCA
Time: O(n)
Space: O(h)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root==None:
            return None
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q
        
        leftAns = self.lowestCommonAncestor(root.left,p,q)
        rightAns = self.lowestCommonAncestor(root.right,p,q)
        
        if leftAns == None and rightAns == None:
            return None
        elif leftAns == None and rightAns is not None:
            return rightAns
        elif leftAns is not None and rightAns is None:
            return leftAns
        else:
            # leftAns is not None and rightAns is not None
            return root