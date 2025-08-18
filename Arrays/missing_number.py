def findMissing(nums):
    nums.sort()
    for i,val in enumerate(nums):
        if i!=val:
            return i
    return -1

nums = []
n = int(input("Enter the Size : "))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)


ans = findMissing(nums)
print("Missing Number is : ",ans)