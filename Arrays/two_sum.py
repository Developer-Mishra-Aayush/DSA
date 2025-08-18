def twoSum(nums,target):
    dict = {}
    for i,val in enumerate(nums):
        if val not in dict:
            dict[val] = i
    
    for i,val in enumerate(nums):
        diff = target - val
        if diff in dict and dict[diff]!=i:
            return [i,dict[diff]]
    return [-1,-1]

nums = []
n = int(input("Enter the Size : "))
for i in range(n):
    element = int(input("Enter Data : "))
    nums.append(element)
target = int(input("Enter the Target : "))

ans = twoSum(nums,target)
print("Two Sum index is ",ans)