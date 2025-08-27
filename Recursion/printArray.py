"""
Title: Print Array using Recursion
Approach: Recursive approach printing each element and calling recursively for next index until end of array
Time: O(n) - where n is the length of array
Space: O(n) - due to recursion stack
"""

def printArray(nums,i):
    if i>=len(nums):
        print()
        return
    else:
        print(nums[i]," ",end="")
        printArray(nums,i+1)

nums = [10,20,30,40,50,60,70,80,90,100]
printArray(nums,0)