def removeDuplicates(nums):
    start = 0
    for i in range(1,len(nums)):
        if nums[start]==nums[i]:
            continue
        else:
            start+=1
            nums[start] = nums[i]
    i = start+1
    while i<len(nums):
        nums[i] = '_'
        i+=1

nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)
print("After removing Duplicates : ",nums)