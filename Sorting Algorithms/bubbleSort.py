"""
Title: Bubble Sort
Approach: Repeatedly swap adjacent elements if they are in the wrong order using nested loops.
Time: O(n^2)
Space: O(1)
"""

def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

nums = [120,10,230,60,90,40,22,25]
bubbleSort(nums)
print("After Bubble Sort : ",nums)