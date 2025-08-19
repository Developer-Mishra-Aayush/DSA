def nearlySorted(nums,target):
    start = 0
    end = len(nums)-1
    while start<=end:
        mid = start + (end-start)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            end = mid -1
        else:
            start = mid + 1
    return -1

nums = [10,3,40,20,50,80,70]
target = 80
ans = nearlySorted(nums,target)
print("Element Found At : ",ans)
# [3,10,20,40,50,70,80]
# [10,3,40,20,50,80,70]