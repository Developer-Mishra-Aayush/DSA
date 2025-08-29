"""
Title: Reverse String (Recursive)
Approach: Swap characters at start/end and recurse inward until pointers cross
Time: O(n)
Space: O(n) - recursion depth
"""

def solve(s,start,end):
    if start>end:
        return ''.join(s)
    else:
        s[start],s[end] =  s[end],s[start]
        start+=1
        end-=1
        ans = solve(s,start,end)
        return ans

def reverseString(s):
    if not s:
        return ''
    else:
        start = 0
        end = len(s)-1
        s = list(s)
        ans = solve(s,start,end)
        return ans

s = "ab-cd"

ans = reverseString(s)
print("Reverse String is : ",ans)