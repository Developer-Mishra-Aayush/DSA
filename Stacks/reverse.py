"""
Title: Reverse Stack using Recursion
Approach: Use recursion to reverse stack by popping all elements and inserting each at bottom during backtrack
Time: O(n^2) where n is the number of elements in stack
Space: O(n) for recursion stack
"""

from collections import deque

def solve(stack,data):
    if not stack:
        stack.append(data)
        return
    else:
        element = stack.pop()
        solve(stack,data)
        stack.append(element)

def reverse(stack):
    if not stack:
        return
    else:
        data = stack.pop()
        reverse(stack)
        solve(stack,data)

stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
print("Stack is ",stack)
reverse(stack)
print("Reverse Stack is : ",stack)