"""
Title: Rotate Array by k (Right Rotation)
Approach: Reverse whole array, then reverse first k elements, then reverse remaining elements (triple-reverse).
Time: O(n)
Space: O(1)
"""

def reverse(nums,start,end):
    while start<=end:
        nums[start],nums[end] = nums[end],nums[start]
        start+=1
        end-=1



def shiftArray(nums,k):
    k = k % len(nums)
    # First Reverse Whole Array
    reverse(nums,0,len(nums)-1)

    # Now Reverse The kth Part Of Array
    reverse(nums,0,k-1)

    # Now Reverse The Remaining Part
    reverse(nums,k,len(nums)-1)



nums = [10,20,30,40,50]
k = int(input("Enter K : "))

shiftArray(nums,k)
print("After Shifting the Array : ",nums)