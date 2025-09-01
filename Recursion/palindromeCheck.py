"""
Title: Palindrome Check
Approach: Use recursion to check if string is palindrome by comparing characters from start and end
Time: O(n) where n is the length of the string
Space: O(n) for recursion stack
"""

def solve(s,start,end):
    if start>end:
        return True
    if s[start]!=s[end]:
        return False
    ans = solve(s,start+1,end-1)
    return ans

def palindromeCheck(s):
    if len(s)<=1:
        return True
    else:
        start = 0
        end = len(s)-1
        ans = solve(s,start,end)
        return ans

s = "Racecar"
s = "NOONNOON"
ans = palindromeCheck(s)
print("Is Palindrome : ",ans)