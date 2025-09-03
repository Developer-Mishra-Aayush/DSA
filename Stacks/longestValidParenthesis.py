"""
Title: Longest Valid Parentheses
Approach: Use a stack of indices; start with -1 as base. Push indices of '('; on ')', pop and compute current valid length as i - stack[-1]; when stack empties, push current index as new base
Time: O(n)
Space: O(n)
"""

from collections import deque

def longestValidParenthesis(s):
    stack = deque()
    stack.append(-1)
    ans = 0
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                temp = i-stack[-1]
                ans = max(ans,temp)
    return ans

s = input("Enter the Parenthesis : ")
ans = longestValidParenthesis(s)
print("Longest Valid Parenthesis is : ",ans)