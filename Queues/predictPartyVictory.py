"""
Title: Dota2 Senate (Predict Party Victory)
Approach: Use two queues to store indices of 'R' and 'D'; simulate rounds by popping the smaller index and appending it with +n to represent the next turn cycle
Time: O(n)
Space: O(n)
"""

from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        r = deque()
        d = deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i]=='R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            r_index = r.popleft()
            d_index = d.popleft()
            if r_index<d_index:
                r.append(r_index+n)
            else:
                d.append(d_index+n)
        return "Radiant" if r else "Dire"