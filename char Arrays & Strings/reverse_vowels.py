def isNotVowels(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if s not in vowels:
        return True
    else:
        return False

def reverseVowels(s):
    s = list(s)
    start = 0
    end = len(s)-1
    while start<=end:
        while start<=end and isNotVowels(s[start]):
            start+=1
        while start<=end and isNotVowels(s[end]):
            end-=1
        if start<=end:
            s[start],s[end] = s[end],s[start]
            start+=1
            end-=1
    return ''.join(s)

s = input("Enter the String : ")
ans = reverseVowels(s)
print("After Reversing the Vowels : ",ans)