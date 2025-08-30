"""
Title: Binary Search using Recursion
Approach: Recursive divide and conquer approach, comparing middle element and searching left or right half accordingly
Time: O(log n) - where n is the length of array
Space: O(log n) - due to recursion stack
"""

def binarySearch(nums,search,start,end):
    mid = start + (end - start)//2
    if start>end:
        return False
    elif nums[mid]==search:
        return mid
    elif nums[mid]>search:
        return binarySearch(nums,search,start,mid-1)
    else:
        return binarySearch(nums,search,mid+1,end)

nums = [10,20,30,40,50,60,70,80,90,100]
search = int(input("Enter the Search Element : "))
ans = binarySearch(nums,search,0,len(nums)-1)
print("Is Element Found : ",ans)