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