"""
Title: Minimum Time to Collect Garbage
Approach: Count pickups for each type and add travel time up to the last house containing that type.
Time: O(n)
Space: O(1)
"""

def garbageCollection(garbage,travel):
    pCollect = 0
    pTravel = 0
    pHouse = 0

    gCollect = 0
    gTravel = 0
    gHouse = 0

    mCollect = 0
    mTravel =0
    mHouse = 0

    for i,data in enumerate(garbage):
        if 'P' in data:
            count = data.count('P')
            pCollect+=count
            pHouse = i

    for i,data in enumerate(garbage):
        if 'G' in data:
            count = data.count('G')
            gCollect+=count
            gHouse = i
            
    for i,data in enumerate(garbage):
        if 'M' in data:
            count = data.count('M')
            mCollect+=count
            mHouse = i

    if pHouse!=0:
        for i in range(pHouse):
            pTravel+=travel[i]
    if gHouse!=0:
        for i in range(gHouse):
            gTravel+=travel[i]
    if mHouse!=0:
        for i in range(mHouse):
            mTravel+=travel[i]

    tTime = pCollect + pTravel + gCollect + gTravel + mCollect + mTravel
    return tTime
    
garbage = ["G","P","GP","GG"]
travel = [2,4,3]
garbage = ["MMM","PGM","GP"]
travel = [3,10]
ans = garbageCollection(garbage,travel)
print("Minimum Time to collect all Garbage is : ",ans)