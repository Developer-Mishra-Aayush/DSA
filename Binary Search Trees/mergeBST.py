"""
Title: Merge Two BSTs into Sorted List
Approach: Simultaneous inorder traversal using two stacks; at each step, pick smaller top, append to result, and traverse its right subtree.
Time: O(n + m)
Space: O(h1 + h2)
"""
from collections import deque

class Solution:
    def merge(self, root1, root2):
        sa = deque()
        sb = deque()
        ans = []
        
        temp1 = root1
        temp2 = root2
        
        while temp1 or temp2 or sa or sb:
            
            while temp1:
                sa.append(temp1)
                temp1 = temp1.left
                
            while temp2:
                sb.append(temp2)
                temp2 = temp2.left
                
            if len(sb)<1 or (len(sa)>=1 and sa[-1].data<=sb[-1].data):
                ans.append(sa[-1].data)
                curr = sa.pop()
                temp1 = curr.right
            
            else:
                ans.append(sb[-1].data)
                curr = sb.pop()
                temp2 = curr.right
            
        return ans