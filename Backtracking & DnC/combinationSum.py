"""
Title: Combination Sum
Approach: Use backtracking to find all combinations of candidates that sum to target
Time: O(2^target) in worst case as we can choose each candidate multiple times
Space: O(target) for recursion stack
"""

def solve(candidates,target,ans,tempAns,index):
    if target==0:
        ans.append(tempAns[:])
        return
    if target<0:
        return
    else:
        for i in range(index,len(candidates)):
            tempAns.append(candidates[i])
            solve(candidates,target-candidates[i],ans,tempAns,i)
            tempAns.pop()

def combinationSum(candidates,target):
    ans = []
    tempAns = []
    solve(candidates,target,ans,tempAns,0)
    return ans

candidates = [2,3,6,7]
target = 7
ans = combinationSum(candidates,target)
print("Ans is : ",ans)