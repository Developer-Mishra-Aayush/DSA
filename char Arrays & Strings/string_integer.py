def isInt(a):
    if a>='0' and a<='9':
        return True
    else:
        return False

def atoi(s):
    ans = 0
    i = 0
    while i<len(s) and i==' ':
        i+=1
    sign = '+'
    if s[i]=='-':
        sign='-'
        i+=1
    while i<len(s) and isInt(s[i]):
        ans = ans*10 + int(s[i])
        i+=1
    if sign=='-':
        return -1*ans
    return ans

s = input("Enter the String : ")
ans = atoi(s)
print("String to integre is : ",ans)