def wave_print(nums):
    ans = []
    for i in range(len(nums)):
        if i%2==0:
            for j in range(0,len(nums)):
                ans.append(nums[j][i])
        else:
            for j in range(len(nums)-1,-1,-1):
                ans.append(nums[j][i])
    return ans

nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]
ans = wave_print(nums)
print("Wave Print of a Matrix is : ",ans)