def row_wise_sum(nums):
    ans = []
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums[0])):
            sum = sum + nums[i][j]
        ans.append(sum)
    return ans

nums = [[1,2,3],
        [4,5,6],
        [7,8,9]]
ans = row_wise_sum(nums)
print("Row Wise Sum is : ",ans)