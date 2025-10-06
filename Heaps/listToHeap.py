"""
Title: Build Max-Heap from List (Heapify In-Place)
Approach: Starting from last non-leaf node, call heapify downward to enforce heap property for all nodes.
Time: O(n)
Space: O(1)
"""

def heapify(l1,index):
    left = index * 2
    right = index * 2 + 1
    largestIndex = index

    if left<len(l1) and l1[left]>l1[largestIndex]:
        largestIndex = left

    if right<len(l1) and l1[right]>l1[largestIndex]:
        largestIndex = right
    
    if largestIndex!=index:
        l1[index],l1[largestIndex] = l1[largestIndex],l1[index]
        heapify(l1,largestIndex)
    


def list_heap(l1):
    for i in range(len(l1)//2-1,-1,-1):
        heapify(l1,i)

l1 = [10,5,20,1,15]
print("Before Heapify : ",l1)
list_heap(l1)
print("After Heapify  : ",l1)