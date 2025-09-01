"""
Title: Partition Equal Subset Sum
Approach: Use recursion to check if array can be partitioned into two subsets with equal sum
Time: O(2^n) where n is the length of the array
Space: O(n) for recursion stack
"""

def solve(nums,sumi,i):
    if i>=len(nums):
        return False
    if sumi >sum(nums)//2:
        return False
    if sumi == sum(nums)//2:
        return True
    ans = 0
    # Exclude Case
    left = solve(nums,sumi,i+1)

    # Include Case
    right = solve(nums,sumi+nums[i],i+1)
    if left or right:
        return True
    else:
        return False

def canPartition(nums):
    if sum(nums)%2!=0 or len(nums)<=1:
        return False
    else:
        ans = solve(nums,0,0)
        return ans

nums = [1,5,11,5]
# nums = [1,2,3,5]
ans = canPartition(nums)
print("Is Partition DOne : ",ans)