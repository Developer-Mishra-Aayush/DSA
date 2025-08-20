def isPossible(stalls,cows,mid):
    cowCount = 1
    prev = stalls[0]
    for i in stalls:
        if i-prev>=mid:
            cowCount+=1
            prev = i
    return cowCount>=cows

def aggressiveCows(stalls,cows):
    minDistance = stalls[0]
    maxDistance = stalls[-1] - stalls[0]
    ans = -1
    for i in range(minDistance,maxDistance+1):
        if isPossible(stalls,cows,i):
            ans = i
        else:
            return ans
    return ans

stalls = [1,2,4,8,9]
cows = 3
ans = aggressiveCows(stalls,cows)
print("Minimum Distance In Which Cows Can be Placed is : ",ans)