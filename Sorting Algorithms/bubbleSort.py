def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

nums = [120,10,230,60,90,40,22,25]
bubbleSort(nums)
print("After Bubble Sort : ",nums)