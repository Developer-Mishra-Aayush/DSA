"""
Title: Combinations
Approach: Use backtracking to generate all possible combinations of k elements from 1 to n
Time: O(C(n,k)) where C(n,k) is the binomial coefficient
Space: O(k) for recursion stack and current combination
"""

class Solution:
    def solve(self,n,k,ans,tempAns,start):
        if k==0:
            ans.append(tempAns[:])
            return
        else:
            for i in range(start,n+1):
                tempAns.append(i)
                self.solve(n,k-1,ans,tempAns,i+1)
                tempAns.pop()


    def combine(self,n,k):
        start = 1
        ans = []
        tempAns = []
        self.solve(n,k,ans,tempAns,start)
        return ans