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