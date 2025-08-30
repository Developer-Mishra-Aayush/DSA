"""
Title: Print All Subarrays
Approach: Fix start index and grow a temporary list to append each subarray [start..end]; move start forward recursively
Time: O(n^3) including copying (O(n^2) subarrays; total copy cost sums to O(n^3))
Space: O(n) auxiliary for current subarray; output storage is O(n^3) total elements across all subarrays
"""

def solve(nums, ans, start):
    if start == len(nums):   # base case
        return
    
    temp = []
    for end in range(start, len(nums)):
        temp.append(nums[end])
        ans.append(temp[:])   # append copy of current subarray
    
    # move to next start index
    solve(nums, ans, start + 1)


def printSubArray(nums):
    ans = []
    solve(nums, ans, 0)
    return ans


nums = [1, 2, 3, 4, 5]
ans = printSubArray(nums)
print("All Subarrays:", ans)