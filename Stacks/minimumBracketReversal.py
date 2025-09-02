"""
Title: Minimum Bracket Reversal
Approach: Use stack to remove balanced pairs; for remaining, reversals = len//2 plus adjustments for mismatches
Time: O(n)
Space: O(n)
"""

from collections import deque

def minimumReversal(s):
    stack = deque()
    if not s:
        return 0
    for i in s:
        if not stack or i=='(':
            stack.append(i)
        elif i==')' and stack[-1]=='(':
            stack.pop()
        else:
            stack.append(i)
    count = 0
    if len(stack)%2!=0:
        return -1
    while stack:
        first = stack.pop()
        second = stack.pop()
        if first == second:
            count+=1
        else:
            count+=2
    return count

s = input("Enter the bracket combination : ")
ans = minimumReversal(s)
print("Minimum Bracket Reversal is : ",ans)