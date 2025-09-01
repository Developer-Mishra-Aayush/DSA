"""
Title: Find Middle Element of Stack
Approach: Calculate middle index and pop elements until reaching the middle element
Time: O(n) where n is the number of elements in stack
Space: O(1) constant extra space
"""

from collections import deque
stack = deque()

def printMiddle(stack,index):
    if not stack:
        return -1
    if len(stack)<=2:
        return stack[-1]
    requiredPop = len(stack)-1 - index
    print()
    while requiredPop!=0:
        stack.pop()
        requiredPop-=1
    return stack[-1]

stack.append('a')
stack.append('b')
stack.append('c')
stack.append('d')
stack.append('e')
ans = printMiddle(stack,len(stack)//2)
print("Middle Element Of A Stack is : ",ans)