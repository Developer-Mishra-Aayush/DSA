"""
Title: Last Occurrence of Character
Approach: Use recursion to find the last occurrence of a target character in the string
Time: O(n) where n is the length of the string
Space: O(n) for recursion stack
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