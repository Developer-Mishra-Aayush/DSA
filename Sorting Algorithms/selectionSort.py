def selectionSort(nums):
    for i in range(len(nums)):
        mini_index = i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[mini_index]:
                mini_index = j
        if mini_index!=i:
            nums[mini_index],nums[i] = nums[i],nums[mini_index]



nums = [120,10,230,60,90,40,22,25]
selectionSort(nums)
print("After Bubble Sort : ",nums)