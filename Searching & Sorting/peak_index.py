def peakIndexInMountainArray(nums):
    start = 0
    end = len(nums)-1
    while start<end:
        mid = start + (end -start)//2
        if nums[mid]<nums[mid+1]:
            start = mid +1
        else:
            end = mid
    return end




nums = [0,2,1,0]
ans = peakIndexInMountainArray(nums)
print("Peak Index In Mountain Array is : ",ans)