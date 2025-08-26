"""
Title: Maximum Subarray (Kadane's Algorithm)
Approach: Maintain running sum; reset to 0 when negative, track maximum seen.
Time: O(n)
Space: O(1)
"""

def maxSubarray(nums):
    maxi = float('-inf')
    sumi = 0
    for i in nums:
        sumi = sumi + i
        maxi = max(maxi,sumi)
        if sumi<0:
            sumi = 0
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
ans = maxSubarray(nums)
print("Maximum SubArray is : ",ans)