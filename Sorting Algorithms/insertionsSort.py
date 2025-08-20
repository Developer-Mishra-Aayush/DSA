def insertionSort(nums):
    for i in range(1,len(nums)):
        j = i-1
        key = nums[i]
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key

nums = [120,10,230,60,90,40,22,25]
insertionSort(nums)
print("After Insertion Sort : ",nums)