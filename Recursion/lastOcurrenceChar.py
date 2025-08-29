"""
Title: Last Occurrence of Character (Recursive)
Approach: Traverse string recursively and update answer when character matches; return the last seen index
Time: O(n)
Space: O(n) - recursion depth
"""

def solve(s,x,ans,index):
    if index>=len(s):
        return ans
    if s[index]==x:
        ans = index
    result = solve(s,x,ans,index+1)
    return result

def lastOccurence(s,x):
    if not s:
        return -1
    index = 0
    ans = -1
    ans = solve(s,x,ans,index)
    return ans

s = "abcddedg"
x = 'd'
ans = lastOccurence(s,x)
print("Last Occurence Of a Character is : ",ans)