"""
Title: Simplify Path (Unix-style)
Approach: Split by '/', use a stack to process '.', '..', and names to build canonical path
Time: O(n)
Space: O(n)
"""

from collections import deque
def simplifyPath(ans):
    stack = deque()
    ans = ans.split('/')
    for i in ans:
        if i=='' or i=='.':
            continue
        elif i=='...':
            stack.append(i)
        elif i=='..':
            if stack:
                stack.pop()
        else:
            stack.append(i)
    return '/' + '/'.join(stack)

path = input("Enter the Path :")
ans = simplifyPath(path)
print("Simplify Path is : ",ans)