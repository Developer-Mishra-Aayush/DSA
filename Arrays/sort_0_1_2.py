"""
Title: Sort 0s, 1s, and 2s (Dutch National Flag)
Approach: Three-pointer partitioning with start, mid, end; swap based on current value.
Time: O(n)
Space: O(1)
"""

def sort_0_1_2(nums):
    start = 0
    mid = 0 
    end = len(nums)-1

    while mid<=end:
        if nums[mid]==0:
            nums[start],nums[mid] = nums[mid],nums[start]
            start+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        elif nums[mid]==2:
            nums[mid],nums[end] = nums[end],nums[mid]
            end-=1

nums = []
n = int(input("Enter the Size : "))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)

sort_0_1_2(nums)
print("After Sorting : ",nums)