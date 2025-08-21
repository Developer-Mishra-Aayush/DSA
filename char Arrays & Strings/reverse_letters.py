def isNotLetter(s):
    if (s>='a' and s<='z') or (s>='A' and s<='Z'):
        return False
    return True

def reverseLetter(s):
    s = list(s)
    start = 0
    end = len(s)-1
    while start<=end:
        while start<=end and isNotLetter(s[start]):
            start+=1
        while start<=end and isNotLetter(s[end]):
            end-=1
        if start<=end:
            s[start],s[end] = s[end],s[start]
            start+=1
            end-=1
    return ''.join(s)

s = input("Enter the String :")
ans = reverseLetter(s)
print("After Reversing Only Letters : ",ans)