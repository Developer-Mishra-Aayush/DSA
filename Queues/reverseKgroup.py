"""
Title: Reverse Queue in Groups of K
Approach: Recursively pop K elements to a temporary array, push them back reversed; process remainder recursively and collect into output deque
Time: O(n)
Space: O(k) auxiliary + O(n) output
"""

from collections import deque

def solve(queue,k,stack):
    if len(queue)<k:
        while queue:
            ans = queue.popleft()
            stack.append(ans)
        return
    else:
        tempAns = []
        i = 0
        while i!=k:
            ans = queue.popleft()
            tempAns.append(ans)
            i+=1
        while tempAns:
            ans = tempAns.pop()
            stack.append(ans)
        solve(queue,k,stack)

def reverseKgroup(queue,k):
    if len(queue)<k:
        return queue
    stack = deque()
    solve(queue,k,stack)
    return stack

queue = deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.append(40)
queue.append(50)
queue.append(60)
queue.append(70)
queue.append(80)
queue.append(90)
ans = reverseKgroup(queue,2)
print("Reversed in K Group is : ",ans)