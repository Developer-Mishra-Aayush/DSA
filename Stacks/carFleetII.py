"""
Title: Car Fleet II
Approach: Traverse cars from right to left using a monotonic stack of candidate fleets; compute collision time with the car ahead and discard candidates that collide later than the new collision time. This yields the first collision time for each car.
Time: O(n)
Space: O(n)
"""

# Implementation can be added here following the documented approach.

from collections import deque

def getCollisionTimes(cars):
    stack = deque()
    ans = [-1 for _ in range(len(cars))]
    i = len(cars)-1
    while i>=0:
        while stack and cars[stack[-1]][1]>=cars[i][1]:
            stack.pop()
        
        if stack:
            pos_i, speed_i = cars[i]
            pos_j, speed_j = cars[stack[-1]]
            ans[i] = (pos_j - pos_i) / (speed_i - speed_j)
        stack.append(i)
        i-=1
    return 

cars = [[1,2],[2,1],[4,3],[7,2]]
ans = getCollisionTimes(cars)
print("Collision Time of Every Car is : ",ans)