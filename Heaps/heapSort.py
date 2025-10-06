def heapify(nums,n,index):
    left = index*2
    right = index*2 + 1

    largestIndex = index

    if left<n and nums[left]>nums[largestIndex]:
        largestIndex = left
    
    if right<n and nums[right]>nums[largestIndex]:
        largestIndex = right

    if largestIndex!=index:
        nums[index],nums[largestIndex] = nums[largestIndex],nums[index]
        heapify(nums,n,largestIndex)



def heap_sort(nums):
    n = len(nums)
    # Step 1 : For heap sort , Create a heap
    for i in range(n//2-1,-1,-1):
        heapify(nums,n,i)

    # Step 2 : One by One extract element from heap and append it into end
    for i in range(n-1,0,-1):
        nums[0],nums[i] = nums[i],nums[0]
        heapify(nums,n,i)




nums = [10,5,20,1,15]
print("Original List is : ",nums)
heap_sort(nums)
print("Sorted Array is : ",nums)