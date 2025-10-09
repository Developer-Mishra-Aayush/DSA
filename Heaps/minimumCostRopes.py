import heapq
class Solution:
    
    def minCost(self, arr):
        if len(arr)==1:
            return 0
        total_cost = []
        heapq.heapify(arr)
        while len(arr)>1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            ans = first + second
            heapq.heappush(arr,ans)
            if len(total_cost)>=1:
                temp = total_cost.pop()
                total_cost.append(temp+ans)
            else:
                total_cost.append(ans)
        return total_cost[-1]