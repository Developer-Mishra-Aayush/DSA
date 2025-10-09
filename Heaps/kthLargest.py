import heapq

def kThLargest(nums,k):
    heap = []
    
    for i in range(k):
        heapq.heappush(heap,nums[i])
    
    for i in range(k,len(nums)):
        if nums[i]>heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,nums[i])
    return heap[0]

nums = []
n = int(input("ENter the Size of the List : "))

for i in range(n):
    element = int(input("Enter the Data : "))
    nums.append(element)

k = int(input("Enter the K : "))
ans = kThLargest(nums,k)
print("K Largest Number using Priority Queue is : ",ans)