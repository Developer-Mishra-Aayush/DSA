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