def solve(candidates,target,ans,tempAns,index):
    if target==0:
        ans.append(tempAns[:])
        return
    if target<0:
        return
    else:
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue
            tempAns.append(candidates[i])
            solve(candidates,target-candidates[i],ans,tempAns,i+1)
            tempAns.pop()

def combinationSum(candidates,target):
    ans = []
    tempAns = []
    candidates.sort()
    solve(candidates,target,ans,tempAns,0)
    return ans

candidates = [2,3,6,7]
target = 7
candidates = [10,1,2,7,6,1,5]
target = 8
ans = combinationSum(candidates,target)
print("Ans is : ",ans)