"""
Title: Binary Search
Approach: Iterative binary search on a sorted array using start, end, and mid pointers.
Time: O(log n)
Space: O(1)
"""

def binary_search(nums,target):
    start = 0
    end = len(nums)-1
    while start<=end:
        mid = start + (end - start)//2
        if nums[mid]==target:
            return True
        elif nums[mid]>target:
            end = mid -1
        else:
            start = mid + 1
    return False

nums = [2,8,10,20,30,34,46,78]
target = 30
ans = binary_search(nums,target)
print("Target Found : ",ans)