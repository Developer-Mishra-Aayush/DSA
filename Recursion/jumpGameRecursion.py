"""
Title: Jump Game (Recursive)
Approach: Use recursion to check if it's possible to reach the end of array using jumps
Time: O(2^n) where n is the length of the array
Space: O(n) for recursion stack
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