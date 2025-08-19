def move_all_negative(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]<0:
            if j!=i:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
            else:
                j+=1

nums = []
n = int(input("Enter The Size : "))
for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)
move_all_negative(nums)
print("After Removing all Negative to Left Side : ",nums)
# -1 2 -3 4 5 6 -4 -4 9 -1