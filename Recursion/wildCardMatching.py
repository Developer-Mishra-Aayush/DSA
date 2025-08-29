def solve(s,t,len1,len2):
    if len1<0 and len2<0:
        return True
    if len1<0 and len2>=0:
        return False
    if len1>=0 and len2<0:
        for j in range(len1,-1,-1):
            if s[j]!='*':
                return False
            j-=1
        return True
    
    else:
        if s[len1]==t[len2] or t[len2]=='?':
            return solve(s,t,len1-1,len2-1)
        elif s[len1]=='*':
            return solve(s,t,len1,len2-1) or solve(s,t,len1-1,len2-1)
        else:
            return False

def isMatch(s,t):
    len1 = len(s)-1
    len2 = len(t)-1
    ans = solve(s,t,len1,len2)
    return ans

s = input("Enter the String : ")
t = input("Enter the String : ")
ans = isMatch(s,t)
print("Is Match : ",ans)