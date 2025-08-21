def isValid(s,t):
    return sorted(s)==sorted(t)

s = input("Enter the String : ")
t = input("Enter the String : ")

ans = isValid(s,t)
print("Is Valid Anagram : ",ans)