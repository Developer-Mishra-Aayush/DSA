"""
Title: Print Subarrays
Approach: Use recursion to generate and print all possible subarrays of the given array
Time: O(2^n) where n is the length of the array
Space: O(n) for recursion stack
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