def findMaxAverage(nums,k):
    max_ans = -1
    if len(nums)<k:
        return max_ans
    for i in range(0,len(nums)-k):
        sumi = sum(nums[i:i+k])
        max_ans = max(sumi,max_ans)
    return max_ans/k

nums = []
n = int(input("Enter the Size : "))
for i in range(n):
    element = int(input("Enter the data : "))
    nums.append(element)
k = int(input("Enter k : "))

ans = findMaxAverage(nums,k)
print("Maximum Average is : ",ans)