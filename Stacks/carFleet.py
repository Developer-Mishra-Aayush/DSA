"""
Title: Car Fleet
Approach: Sort cars by starting position descending; compute time to target; use a stack to merge cars that catch up (non-decreasing times form fleets)
Time: O(n log n) for sorting
Space: O(n) for stack
"""
from collections import deque
def carFleet(target,position,speed):
    stack = deque()
    dict = {}
    for i in range(len(position)):
        dict[position[i]] = speed[i]
    sPosition = sorted(dict)
    timeTaken = []
    for i in range(len(sPosition)):
        # t = d/s
        d = target-sPosition[i]
        timeTaken.append(d//(dict[sPosition[i]]))

    for i in timeTaken:
        if not stack:
            stack.append(i)
        elif i>=stack[-1]:
            while i>=stack[-1]:
                stack.pop()
            stack.append(i)
        else:
            stack.append(i)
    return len(stack)

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
ans = carFleet(target,position,speed)
print("Total Fleet is : ",ans)