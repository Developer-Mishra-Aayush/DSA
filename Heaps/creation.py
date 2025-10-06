"""
Title: Max Heap Implementation (Insert/Delete/Heapify)
Approach: Array-based binary heap; insert by percolate-up, delete max by swap with last and heapify-down.
Time: Insert/Delete O(log n); Heapify O(log n)
Space: O(n)
"""

class Heap:
    def __init__(self):
        self.heap = []
    
    def parent(self,i):
        return (i-1)//2
    
    def insert(self,data):
        self.heap.append(data)

        i = len(self.heap)-1
        while i!=0 and self.heap[self.parent(i)]<self.heap[i]:
            # If Parent Node is Smaller than swap it
            self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
            i = self.parent(i)

    def delete(self):
        if len(self.heap)==0:
            return
        if len(self.heap)==1:
            element = self.heap.pop()
            return element
        else:
            element = self.heap[0]
            self.heap[0] = self.heap.pop()
            self.heapify(0)
            return element
    
    def heapify(self,index):
        left = index*2
        right =index*2 + 1
        largestindex = index

        if left<len(self.heap) and self.heap[left]>self.heap[largestindex]:
            largestindex = left
        if right<len(self.heap) and self.heap[right]>self.heap[largestindex]:
            largestindex = right

        if largestindex!=index:
            self.heap[index],self.heap[largestindex] = self.heap[largestindex],self.heap[index]
            self.heapify(largestindex)
    


pq = Heap()
pq.insert(10)
pq.insert(20)
pq.insert(5)
ans = pq.delete()
print("Deleted Element is : ",ans)
print("Heap is : ",pq.heap)