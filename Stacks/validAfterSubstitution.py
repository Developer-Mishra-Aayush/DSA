"""
Title: Check if String is Valid After Substitutions (abc)
Approach: Recursively remove occurrences of 'abc' until no more; valid if empty at end
Time: O(k * n) worst-case where k removals, n length
Space: O(k) recursion depth
"""

def isValid(s):
    if not s:
        return True
    elif s.find('abc')!=-1:
        s = s.replace('abc','')
        return isValid(s)
        print("Hello")
    else:
        return False

s = input("Enter the String : ")

ans = isValid(s)
print("IS Valid After Substitution : ",ans)