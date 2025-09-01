"""
Title: In-place Merge Sort
Approach: Use divide and conquer to sort array in-place by merging sorted subarrays
Time: O(n log n) where n is the length of array
Space: O(1) additional space (in-place)
"""

import math

def findGap(totalLen):
    if totalLen<=1:
        return 0
    else:
        return math.ceil(totalLen/2) 

def inplace_merge(arr,start,mid,end):
    totalLen = end - start + 1
    gap = findGap(totalLen)
    
    while gap > 0:
        i= start
        j = start + gap
        while j<end:
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j+=1
        gap = findGap(gap)

def inplace_merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        inplace_merge_sort(arr, start, mid)
        inplace_merge_sort(arr, mid + 1, end)
        inplace_merge(arr, start, mid, end)

nums = [2, 4, 1, 3, 5]
inplace_merge_sort(nums, 0, len(nums) - 1)
print("Sorted Array:", nums)