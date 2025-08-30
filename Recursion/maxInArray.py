"""
Title: Find Maximum in Array using Recursion
Approach: Recursive approach comparing each element with current maximum, updating max when larger element found
Time: O(n) - where n is the length of array
Space: O(n) - due to recursion stack
"""

def findMaxRecursive(nums,maxi,start):
    if start>=len(nums):
        return maxi
    if nums[start]>maxi:
        maxi = nums[start]
    return findMaxRecursive(nums,maxi,start+1)

nums = [10,203,112,203,123,45,60]
ans = findMaxRecursive(nums,float('-inf'),0)
print("Maximum In An Array is : ",ans)