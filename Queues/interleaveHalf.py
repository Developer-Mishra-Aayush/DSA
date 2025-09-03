from collections import deque

def interLeaveHalf(queue):
    q1 = deque()
    k = len(queue)//2
    i = 0
    while i<k:
        ans = queue.popleft()
        q1.append(ans)
        i+=1
    while q1:
        ans = q1.popleft()
        queue.append(ans)
        ans = queue.popleft()
        queue.append(ans)

queue = deque()
queue.append(20)
queue.append(40)
queue.append(80)
queue.append(10)
queue.append(30)
queue.append(50)

interLeaveHalf(queue)
print(queue)