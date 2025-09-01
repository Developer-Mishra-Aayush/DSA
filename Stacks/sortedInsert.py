"""
Title: Insert Element in Sorted Stack
Approach: Use recursion to maintain sorted order by finding correct position and inserting element
Time: O(n) where n is the number of elements in stack
Space: O(n) for recursion stack
"""

from collections import deque
stack = deque()

def insertSorted(stack,data):
    if stack[-1]<=data:
        stack.append(data)
        return
    else:
        element = stack.pop()
        insertSorted(stack,data)
        stack.append(element)

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
insertSorted(stack,24)
print("Stack is : ",stack)