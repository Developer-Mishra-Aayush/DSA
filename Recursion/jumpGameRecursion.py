"""
Title: Jump Game (Recursive Reachability)
Approach: From current index, try all jumps from 1..nums[i] recursively; return True if any path reaches last index
Time: Exponential without memoization
Space: O(n) - recursion depth in worst case
"""

def solve(nums,index):
    if index == len(nums)-1:
        return True
    if index>=len(nums):
        return False
    if nums[index]==0:
        return False
    else:
        for j in range(1,nums[index]+1):
            ans = solve(nums,index+j)
    return ans

def canJump(nums):
    i =0
    ans = solve(nums,i)
    return ans

nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
ans = canJump(nums)
print("Able to Jump at Last index : ",ans)