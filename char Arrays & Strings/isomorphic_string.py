"""
Title: Isomorphic Strings
Approach: Ensure a one-to-one mapping from characters in s to t and no two characters map to the same character.
Time: O(n)
Space: O(1) (limited alphabet)
"""

def isIsomorphic(s,t):
    if len(s)!=len(t):
        return False
    s = list(s)
    t = list(t)
    dict = {}
    for i,data in enumerate(s):
        if data not in dict:
            if s[i] in dict.keys():
                return False
            else:
                dict[data] = t[i]
        if data in dict and dict[data]!=t[i]:
            return False
    return True

s = input("Enter the String : ")
t = input("Enter the String : ")
ans = isIsomorphic(s,t)
print("Is Isomorphic String : ",ans)