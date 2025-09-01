"""
Title: Merge Sort
Approach: Use divide and conquer to sort array by recursively dividing into halves and merging sorted halves
Time: O(n log n) where n is the length of array
Space: O(n) for temporary array and recursion stack
"""

def merge(nums,start,end):
    mid = start + (end - start)//2
    len1 = mid - start + 1
    len2 = end - mid
    first = []
    second = []
    mainArrayIndex = start
    for i in range(len1):
        first.append(nums[mainArrayIndex])
        mainArrayIndex+=1
    for i in range(len2):
        second.append(nums[mainArrayIndex])
        mainArrayIndex+=1

    mainArrayIndex = start
    index1 = 0
    index2 = 0
    while index1<len1 and index2<len2:
        if first[index1]<=second[index2]:
            nums[mainArrayIndex] = first[index1]
            index1+=1
        else:
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


def mergeSort(nums,start,end):
    if start < end:
        mid = start + (end - start)//2
        mergeSort(nums,start,mid)
        mergeSort(nums,mid+1,end)

        merge(nums,start,end)

nums = [120,10,230,60,90,40,22,25]
mergeSort(nums,0,len(nums)-1)
print("After Megre Sort : ",nums)