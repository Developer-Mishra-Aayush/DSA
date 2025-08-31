def merge(nums,start,end):
    mid = start + (end - start)//2
    len1 = mid - start + 1
    len2 = end - mid
    mainArrayIndex = start
    first = []
    second = []
    inv = 0
    for i in range(len1):
        first.append(nums[mainArrayIndex])
        mainArrayIndex+=1
    for i in range(len2):
        second.append(nums[mainArrayIndex])
        mainArrayIndex+=1
    
    index1 = 0
    index2 = 0
    mainArrayIndex = start
    while index1<len1 and index2<len2:
        if first[index1]<=second[index2]:
            nums[mainArrayIndex] = first[index1]
            index1+=1
        else:
            inv+= len1 - index1
            nums[mainArrayIndex] = second[index2]
            index2+=1
        mainArrayIndex+=1
    
    while index1<len1:
        nums[mainArrayIndex] = first[index1]
        index1+=1
        mainArrayIndex+=1
    while index2<len2:
        nums[mainArrayIndex] = second[index2]
        index2+=1
        mainArrayIndex+=1
    return inv

def merge_sort(nums,start,end):
    inversion = 0
    if start>=end:
        return inversion
    if start<end:
        mid = start + (end - start)//2
        inversion+=merge_sort(nums,start,mid)
        inversion+=merge_sort(nums,mid+1,end)
        inversion+=merge(nums,start,end)
        return inversion

nums = [2,4,1,3,5]
ans = merge_sort(nums,0,len(nums)-1)
print("Sorted Array is : ",nums)
print("Total Count Inversion is : ",ans)