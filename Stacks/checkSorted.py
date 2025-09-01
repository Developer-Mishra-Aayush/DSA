"""
Title: Check if Stack is Sorted
Approach: Use recursion to check if stack elements are in ascending order from bottom to top
Time: O(n) where n is the number of elements in stack
Space: O(n) for recursion stack
"""

from collections import deque
stack = deque()

def solve(stack,data):
    if not stack:
        return True
    else:
        temp = stack.pop()
        if temp>data:
            print("Hello")
            return False
        return solve(stack,temp)

def isSorted(stack):
    if len(stack)<=1:
        return True
    data = stack.pop()
    ans = solve(stack,data)
    return ans

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
print("Stack is : ",stack)
ans = isSorted(stack)
print("Is Sorted Stack : ",ans)