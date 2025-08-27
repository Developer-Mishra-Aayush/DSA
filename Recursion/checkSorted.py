"""
Title: Check if Array is Sorted using Recursion
Approach: Recursive approach comparing adjacent elements, returning False if current > next, True if end reached
Time: O(n) - where n is the length of array
Space: O(n) - due to recursion stack
"""

def isSorted(nums,start):
    if start>=len(nums)-1:
        if nums[start]>=nums[start-1]:
            return True
        return False
    elif nums[start]>=nums[start+1]:
        return False
    else:
        return isSorted(nums,start+1)

nums = [10,15,25,35,60,95]

ans = isSorted(nums,0)
print("Is Sorted :",ans)