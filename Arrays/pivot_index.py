def pivotIndex(nums):
    first = []
    sum = 0
    for i,val in enumerate(nums):
        sum+=val
        first.append(sum)
    second = []
    sum = 0
    for i in range(len(nums)-1,-1,-1):
        sum+=nums[i]
        second.insert(0,sum)
    print("First is : ",first)
    print("second is : ",second)

    for i in range(len(nums)):
        if first[i]==second[i]:
            return i
    return -1

nums = []
n = int(input("Enter the Size : "))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)
ans = pivotIndex(nums)
print("Pivot Index is : ",ans)