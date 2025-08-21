def expandAroundCenter(s,start,end):
    while start>=0 and end<len(s) and s[start]==s[end]:
        start-=1
        end+=1
    return s[start+1:end]

def longestPalindrome(s):
    if len(s)<=1:
        return s
    maxString = s[0]
    for i in range(len(s)-1):
        odd = expandAroundCenter(s,i,i)
        even = expandAroundCenter(s,i,i+1)
        if len(odd)>len(maxString):
            maxString = odd
        if len(even)>len(maxString):
            maxString = even
    return maxString

s = input("Enter the String : ")
ans = longestPalindrome(s)
print("Longest Palindromic Substring is : ",ans)