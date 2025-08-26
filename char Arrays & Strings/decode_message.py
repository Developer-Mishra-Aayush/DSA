"""
Title: Decode the Message (Substitution Cipher)
Approach: Build a mapping from first appearance in key to 'a'..'z' order, then translate message preserving spaces.
Time: O(n)
Space: O(1) extra (map of at most 26)
"""

def decodeMessage(key,message):
    secret = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','x']
    i = 0
    index = 0
    dict = {}
    while i<len(key) and index<len(secret):
        if key[i]==' ' or key[i] in dict:
            i+=1
        else:
            dict[key[i]] = secret[index]
            i+=1
            index+=1
    ans = ""
    for i in message:
        if i==' ':
            ans+=i
        else:
            ans+=dict[i]
    return ans

key = input("Enter the Key : ")
message = input("Enter the Message : ")
ans = decodeMessage(key,message)
print("Decoded Message is : ",ans)