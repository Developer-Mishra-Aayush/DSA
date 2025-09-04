"""
Title: Reverse a Queue using Recursion
Approach: Recursively pop front element, reverse remainder, then append element at back
Time: O(n)
Space: O(n) recursion
"""

from collections import deque

def reverseQueue(queue):
    if not queue:
        return 
    else:
        element = queue.popleft()
        reverseQueue(queue)
        queue.append(element)

queue = deque()
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')
queue.append('e')
reverseQueue(queue)
print(queue)