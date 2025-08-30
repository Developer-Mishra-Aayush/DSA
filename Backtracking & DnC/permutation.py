def solve(s,ans,tempAns,i):
    if i>=len(s):
        ans.append("".join(tempAns))
        tempAns = s.copy()
        return
    else:
        for j in range(i,len(s)):
            print("I is ",i," J is ",j)
            tempAns[i],tempAns[j] = tempAns[j],tempAns[i]
            solve(s,ans,tempAns,j+1)




def permutation(s):
    ans = []
    s = list(s)
    tempAns = s.copy()
    solve(s,ans,tempAns,0)
    return ans



s = "ab"
ans = permutation(s)
print("Total Possible Permutation is : ",ans)