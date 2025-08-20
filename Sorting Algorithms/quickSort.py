def getPivot(nums,start,end):
    mid = start + (end - start)//2
    pivot = nums[start]

    # Count the Occurence of Smaller Element as Compared to Pivot
    count = 0
    for i in range(start,end+1):
        if nums[i]<=pivot:
            count+=1
    pivotIndex = count + start -1

    # Swap their Position
    nums[start],nums[pivotIndex] = nums[pivotIndex],nums[start]
    index1 = start
    index2 = end
    while index1<pivotIndex and index2>pivotIndex:
        while nums[index1]<=pivot:
            index1+=1
        while nums[index2]>pivot:
            index2-=1
        if index1 < pivotIndex and index2>pivotIndex:
            nums[index1],nums[index2] = nums[index2],nums[index1]
            index1+=1
            index2-=1
    return pivotIndex

def quickSort(nums,start,end):
    mid = start + (end - start)//2
    if start<end:
        pivotIndex = getPivot(nums,start,end)
        quickSort(nums,start,pivotIndex-1)
        quickSort(nums,pivotIndex+1,end)

nums = [120,10,230,60,90,40,22,25]
quickSort(nums,0,len(nums)-1)
print("After Quick Sort : ",nums)