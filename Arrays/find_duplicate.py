def find_duplicate(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    for i in dict:
        if dict[i]>1:
            return i
    return -1

nums = []
n = int(input("Enter the Size :"))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)
ans = find_duplicate(nums)
print("Duplicate Number is : ",ans)