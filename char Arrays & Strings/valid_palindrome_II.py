def isPalindrome(s,start,end):
    while start<=end:
        if s[start]!=s[end]:
            return False
        else:
            start+=1
            end-=1
    return True

def validPalindrome(s,start,end):
    while start<end:
        if s[start]==s[end]:
            start+=1
            end-=1
        else:
            return isPalindrome(s,start+1,end) or isPalindrome(s,start,end-1)
    return True

s = input("Enter the String : ")
ans = validPalindrome(s,0,len(s)-1)
print("Is Palindrome : ",ans)