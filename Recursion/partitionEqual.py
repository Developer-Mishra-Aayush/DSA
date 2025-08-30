"""
Title: Partition Equal Subset Sum (Recursive)
Approach: Recursive inclusion-exclusion to reach sum(nums)//2; prune if sum exceeds or index out of bounds; base when partial sum equals target
Time: Exponential without memoization; worst-case explores 2^n subsets
Space: O(n) - recursion depth
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