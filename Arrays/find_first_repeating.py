def first_repeating_element(nums):
    dict = {}
    for i in nums:
        if i in dict:
            return i
        else:
            dict[i] = 1
    return -1

nums = []
n = int(input("Enter the Size ; "))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)
ans = first_repeating_element(nums)
print("First Repeating Element is : ",ans)