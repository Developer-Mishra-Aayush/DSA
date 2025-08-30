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