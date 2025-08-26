"""
Title: Painter's Partition Problem
Approach: Binary search the maximum time per painter; greedily accumulate boards until exceeding mid, then allocate new painter.
Time: O(n log S) where S is sum of board lengths
Space: O(1)
"""

def isPossible(nums,mid,k):
    studentCount = 1
    pageSum = 0
    for i in range(0,len(nums)):
        if pageSum + nums[i]<=mid:
            pageSum+=nums[i]
        else:
            studentCount+=1
            if studentCount>k or nums[i]>mid:
                return False
            else:
                pageSum = nums[i]
    return True

def splitArray(nums,k):
    start = 0
    end = sum(nums)
    ans = -1
    while start<=end:
        mid = start + (end - start) //2
        if isPossible(nums,mid,k):
            end = mid - 1
            ans = mid
        else:
            start = mid + 1
    return ans

nums = [7,2,5,10,8]
k = 2
nums = [1,2,3,4,5]
k = 2
ans = splitArray(nums,k)
print("Ans is : ",ans)