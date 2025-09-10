"""
Title: Binary Tree Zigzag Level Order Traversal
Approach: BFS with queue collecting each level; reverse alternate levels by toggling a flag
Time: O(n)
Space: O(n)
"""

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.left_to_right = True

    def zigzagLevelOrder(self, root):
        ans = []
        queue = deque()
        
        if root is None:
            return ans
        queue.append(root)

        while queue:
            tempAns = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                tempAns.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not self.left_to_right:
                tempAns.reverse()
            ans.append(tempAns)
            self.left_to_right = not self.left_to_right
        return ans