def singleNumber(nums):
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i]= 1
        else:
            dict[i]+=1
    for i in dict:
        if dict[i]==1:
            return i
    else:
        return -1

nums = [1,2,3,1,2,3,4]
ans = singleNumber(nums)
print("Single Number is : ",ans)