"""
Title: Jump Game II (Recursive Minimum Jumps)
Approach: From current index, try all reachable next indices and take the minimum number of steps to reach end; track steps along recursion
Time: Exponential without memoization
Space: O(n) - recursion depth in worst case
"""

def solve(nums,index,ans,step):
    if index == len(nums)-1:
        ans = min(ans,step)
        return ans
    if index>=len(nums):
        return False
    if nums[index]==0:
        return False
    else:
        for j in range(1,nums[index]+1):
            ans = solve(nums,index+j,ans,step+1)
    return ans

def canJump(nums):
    i =0
    ans = float('inf')
    step = 0
    ans = solve(nums,i,ans,step)
    return ans

nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
ans = canJump(nums)
print("Able to Jump at Last index : ",ans)