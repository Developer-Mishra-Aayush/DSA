"""
Title: Minimum Add to Make Parentheses Valid
Approach: Use stack to match valid parentheses pairs; count remaining unmatched parentheses
Time: O(n) where n is the length of string
Space: O(n) for stack
"""

from collections import deque

def minAddToMakeValid(s):
    stack = deque()
    for i in s:
        if i=='(':
            stack.append(i)
        elif stack and i==')' and stack[-1]=='(':
            stack.pop()
            print(stack)
        else:
            stack.append(i)
    return len(stack)



s = input("Enter the String : ")
ans = minAddToMakeValid(s)
print("Minimum Parenthesis adding to amke it valid is : ",ans)