import heapq
class Solution:
    #Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # code here
        # return merged list
        heap = []
        result = []
        for element in arr:
            for i in element:
                heapq.heappush(heap,i)
        while heap:
            temp = heapq.heappop(heap)
            result.append(temp)
        return result