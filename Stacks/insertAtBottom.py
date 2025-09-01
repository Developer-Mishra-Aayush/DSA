"""
Title: Insert Element at Bottom of Stack
Approach: Use recursion to pop all elements, insert new element, then push back all elements
Time: O(n) where n is the number of elements in stack
Space: O(n) for recursion stack
"""

from collections import deque
stack = deque()

def insertAtBottom(stack,data):
    if not stack:
        stack.append(data)
        return
    else:
        element = stack.pop()
        insertAtBottom(stack,data)
        stack.append(element)

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
insertAtBottom(stack,'A')
print("Stack is : ",stack)