"""
Title: Next Greater Node in Linked List
Approach: Convert to array, then use a monotonic decreasing stack of indices to fill next greater values
Time: O(n)
Space: O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from collections import deque

class Solution:
    def nextLargerNodes(self, head):
        ans = []
        temp = head
        stack = deque()
        while temp:
            ans.append(temp.val)
            temp = temp.next
        for i in range(len(ans)):
            if not stack:
                stack.append(i)
            elif ans[i]>ans[stack[-1]]:
                while stack and ans[i]>ans[stack[-1]]:
                    ans[stack[-1]] = ans[i]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)
        while stack:
            ans[stack[-1]] = 0
            stack.pop()
        return ans