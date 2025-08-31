def maxSubArray(nums):
    maxi = nums[0]
    sum = 0
    for i in range(len(nums)):
        sum+=nums[i]
        if sum<0:
            sum = 0
        else:
            maxi = max(sum,maxi)
    return maxi

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
ans = maxSubArray(nums)
print("Maximum Sub Array Is : ",ans)