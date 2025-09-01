"""
Title: Reverse String
Approach: Use recursion to swap characters from start and end, moving towards center
Time: O(n) where n is the length of the string
Space: O(n) for recursion stack
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