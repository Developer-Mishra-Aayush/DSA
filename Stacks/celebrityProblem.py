"""
Title: Celebrity Problem
Approach: Use stack to eliminate non-celebrities pairwise; verify candidate by row/column checks
Time: O(n) to find candidate + O(n) verify = O(n)
Space: O(n) for stack
"""

from collections import deque

def celebrity_problem(celebrity):
    stack = deque()
    for i in range(len(celebrity)):
        stack.append(i)
    while len(stack)!=1:
        first = stack.pop()
        second = stack.pop()
        if celebrity[first][second]:
            stack.append(second)
        else:
            stack.append(first)
    ans = stack[-1]
    for i in range(celebrity[0]):
        if celebrity[ans][i]==1:
            return -1
    return ans

celebrity = [[0,0,1,0],
             [0,0,1,0],
             [0,0,0,0],
             [0,0,1,0]]
ans = celebrity_problem(celebrity)
print("Celebrity is : ",ans)