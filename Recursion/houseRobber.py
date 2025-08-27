"""
Title: House Robber (Recursive)
Approach: Recursive choice at each index: include current house value and skip next, or exclude current and move to next; take max of both
Time: O(2^n) - exponential without memoization
Space: O(n) - due to recursion stack
"""

def rob(nums,index):
    if index>=len(nums):
        return 0
    else:
        # Exclude Case
        exc = rob(nums,index+1)

        # Include Case
        inc = nums[index]+ rob(nums,index+2)

        return max(inc,exc)

nums = [1,2,3,1]
nums = [2,7,9,3,1]
ans = rob(nums,0)
print("The Maximum You can Robbed is : ",ans)