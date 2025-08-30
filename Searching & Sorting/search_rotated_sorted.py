"""
Title: Search in Rotated Sorted Array
Approach: Find pivot (maximum) via binary search, then binary search in the appropriate half depending on target.
Time: O(log n)
Space: O(1)
"""

def getPivot(nums,target):
    start = 0
    end = len(nums)-1
    while start<end:
        mid = start + (end - start)//2
        if nums[mid]<nums[mid+1]:
            start = mid + 1
        else:
            end = mid
    return end

def binarySearch(nums,start,end,target):
    while start<=end:
        mid = start +(end-start)//2
        if nums[mid]==target:
            return True
        elif nums[mid]>target:
            end = mid -1
        else:
            start = mid + 1
    return False

def search(nums,target):
    pivot = getPivot(nums,target)
    if target>nums[pivot] and nums[pivot+1]:
        return False
    elif target>=nums[pivot+1] and target<nums[0]:
        return binarySearch(nums,pivot+1,len(nums)-1,target)
    else:
        return binarySearch(nums,0,pivot,target)

nums = [4,5,6,7,0,1,2]
target = 0
ans = search(nums,target)
print("Element Found : ",ans)