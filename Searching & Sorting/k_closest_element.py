def k_closest_element(nums,k,x):
    ans = nums.copy()
    for i in range(len(ans)):
        ans[i] = abs(ans[i] - x)

    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if ans[j]>ans[j+1]:
                ans[j],ans[j+1] = ans[j+1],ans[j]
                nums[j],nums[j+1] = nums[j+1],nums[j]
            elif ans[j]==ans[j+1] and nums[j]>nums[j+1]:
                ans[j],ans[j+1] = ans[j+1],ans[j]
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums[0:k]

nums = [1,2,3,4,5]
k = 4
x = 3
ans = k_closest_element(nums,k,x)
print("K Closest Element is : ",ans)