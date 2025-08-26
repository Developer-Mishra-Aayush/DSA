"""
Title: Palindromic Substrings (Count)
Approach: For each center (char and between chars), expand while equal to count palindromes.
Time: O(n^2)
Space: O(1)
"""

def expandAroundCenter(s,start,end):
    count = 0
    while start>=0 and end<len(s) and s[start]==s[end]:
        start-=1
        end+=1
        count+=1
    return count

def countSubstrings(s):
    if len(s)<=1:
        return len(s)
    totalLength = 0
    for center in range(len(s)):
        odd = expandAroundCenter(s,center,center)
        even = expandAroundCenter(s,center,center+1)
        totalLength = totalLength + odd + even
    return totalLength

s = input("Enter the String :")
ans = countSubstrings(s)
print("Total Palindromic Substring is :",ans)