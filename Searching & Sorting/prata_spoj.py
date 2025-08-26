"""
Title: PRATA - Roti Prata (SPOJ)
Approach: Binary search on time; for a given time, simulate how many parathas each cook can make using arithmetic progression of times.
Time: O(cooks * sqrt(T)) per check roughly; overall O(cooks * log answer)
Space: O(1)
"""

def isPossible(cooks,totalParathas,mid):
    tp = 0
    for i in cooks:
        totalTime = 0
        position = 1
        while (totalTime + position*i)<=mid and tp!=totalParathas:
            totalTime = totalTime + position*i
            position+=1
            tp+=1
            if tp==totalParathas:
                return True
    return False

def isMakable(cooks,totalParathas):
    cooks.sort()
    start = 1
    ans = -1
    end = cooks[-1]*(totalParathas*(totalParathas+1)//2)
    while start<=end:
        mid = start + (end - start)//2
        if isPossible(cooks,totalParathas,mid):
            end = mid -1
            ans = mid
        else:
            start = mid + 1
    return ans

cooks = [1,2,3,4]
totalPrathas = 10
ans = isMakable(cooks,totalPrathas)
print("minimum Minutes taken by Cook to make parathas : ",ans)