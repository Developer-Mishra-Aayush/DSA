"""
Title: Linear Search using Recursion
Approach: Recursive approach checking each element sequentially, returning True if found or False if end reached
Time: O(n) - where n is the length of array
Space: O(n) - due to recursion stack
"""

def isFound(nums,search,index):
    if index>=len(nums):
        return False
    if nums[index]==search:
        return True
    else:
        index+=1
        ans = isFound(nums,search,index)
        return 

nums = [10,20,30,40,50]
search = int(input("Enter the Element :"))
ans = isFound(nums,search,0)
print("Is Search Element Found : ",ans)