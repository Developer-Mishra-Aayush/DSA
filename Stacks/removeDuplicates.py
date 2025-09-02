"""
Title: Remove All Adjacent Duplicates in String
Approach: Use stack to remove adjacent equal characters by pushing and popping accordingly
Time: O(n)
Space: O(n)
"""

from collections import deque

def removeDuplicates(s):
    stack = deque()
    if not s:
        return ''
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    return stack

s = input("Enter the String : ")
ans = removeDuplicates(s)
print("After Removing the Duplicates String : ",ans)