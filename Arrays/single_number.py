def singleNumber(nums):
    sum = 0
    for i in nums:
        sum = sum ^i
    return sum

nums = []
n = int(input("Enter the N : "))
for i in range(n):
    element = int(input("Enter the Number : "))
    nums.append(element)

ans = singleNumber(nums)
print("Single Number is : ",ans)