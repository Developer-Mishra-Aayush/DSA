"""
Title: EKO - Spoj (Cutting Trees)
Approach: Binary search on the saw height; sum wood collected at a given height to check if requirement is met.
Time: O(n log H) where H is max tree height
Space: O(1)
"""

def isPossible(trees,r,mid):
    totalWood = 0
    for i in trees:
        if i>=mid:
            totalWood+=(i-mid)
    return totalWood>=r

def solve(trees,r):
    start = 0
    end = max(trees)
    ans = -1
    while start<=end:
        mid = start + (end - start)//2
        if isPossible(trees,r,mid):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

trees = []
n = int(input("Enter the Number of Tree : "))
for i in range(n):
    element = int(input("Enter the Height : "))
    trees.append(element)
r = int(input("Enter the Required Height : "))
ans = solve(trees,r)
print("The Height of the Mirko's Machine is : ",ans)


# 0 20